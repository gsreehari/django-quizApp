from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import requests
from .models import Quiz, Question, Answer, QuizTaker
from .aditionalViews.auth import authSignup,authSignin, authSignOut
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

quiz_questions_list = []


def signinPage(request):
    if request.user.is_authenticated:
        return redirect("quizApp-home")
    else:
        return render(request,"quizApp/signin.html")

def signupPage(request):
    if request.user.is_authenticated:
        return redirect("quizApp-home")
    else:
        return render(request,"quizApp/signup.html")

def home(request):
    user = request.user
    quizlist = []
    quizes = Quiz.objects.filter(active = True)

    for quiz in quizes:
        new_quiz = {}
        try:
            quiz_taker = QuizTaker.objects.filter(user = user, quiz = quiz)[0]
            new_quiz['quiz'] = quiz
            new_quiz['completed'] = True if quiz_taker.completed == True else False
        except:
            new_quiz['quiz'] = quiz
            new_quiz['completed'] = False
        quizlist.append(new_quiz)
    
    return render(request, "quizApp/home.html", {"list": quizlist})


def quizPage(request, quizId):
    
    quiz = Quiz.objects.get(id=quizId)
    questions_list = list(Question.objects.filter(quiz=quiz.pk))
    index = 1
    result_list = []
    quiz_taker = QuizTaker.objects.filter(user = request.user, quiz = quiz)

    if len(quiz_taker) > 0:
        quiz_taker = quiz_taker[0]
        if quiz_taker.completed:
            return render(request,"quizApp/quiz.html", {"completed":quiz_taker.completed, "score":quiz_taker.score,"totalscore":quiz.quizScore})
    else:
        for question in questions_list:
            question_array = {}
            question_array['index'] = index
            question_array['id'] = question.pk
            question_array['question'] = question.label
            answers_list = list(Answer.objects.filter(question=question.pk))
            question_array['options'] = answers_list
            result_list.append(question_array)
            index = index+1
        
        result_list = list(reversed(result_list))
        question_list_length = len(questions_list)
        question_list_length_array = list(range(1,question_list_length+1))
    
        return render(request,"quizApp/quiz.html", {"completed":False, "quiz":quiz,"list": result_list,"length":question_list_length, "lengtharray":question_list_length_array})




#  API PART



def checkAnswer(request):
    questionid = request.GET.get('questionId')
    quizid = request.GET.get('quizId')
    selected_options_list = list(map(int,request.GET.getlist('selectedOptions[]')))

    # res = requests.get('https://opentdb.com/api.php?amount=10&type=multiple',headers={'Content-Type':'application/json'})   
    # geodata = res.json()['results']
    quiz = Quiz.objects.get(id = quizid)
    quiz_taker = QuizTaker.objects.filter(user = request.user, quiz = quiz)

    

    question = Question.objects.get(id=questionid)
    question_mark = question.questionMarks
    answers_list = list(Answer.objects.filter(question=question.pk).filter(isCorrect = True))
    each_answer_marks = question_mark/len(answers_list)
    correct_answers_list = []

    total_marks_obtained = 0.0
    correct = ""

    if len(quiz_taker) == 0:
        quiz_taker = QuizTaker.objects.create(user = request.user, quiz = quiz)
    else:
        quiz_taker = quiz_taker[0]
        total_marks_obtained = quiz_taker.score
    
    for item in answers_list:
        correct_answers_list.append(item.pk)
        if item.pk in selected_options_list:
            total_marks_obtained = total_marks_obtained + each_answer_marks
            correct = item.pk
    
    quiz_taker.score = total_marks_obtained
    quiz_taker.save()

    
    return JsonResponse({"score":total_marks_obtained,"correct":correct, "correct_answers":correct_answers_list},safe=True)


@csrf_exempt
def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    auth_res = authSignup(username,password)

    if auth_res['code'] == "SUS":
        return redirect("quizApp-signin")

    return JsonResponse(auth_res,safe=True)

@csrf_exempt
def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
        # auth_res = authSignin(username,password,request)
    auth_res = authSignin(username,password,request)

    return JsonResponse(auth_res)

@csrf_exempt
def signout(request):
    auth_res = authSignOut(request)

    return JsonResponse(auth_res)

@csrf_exempt
def quizAttempted(request):
    quizid = request.POST.get('quizId')
    quiz = Quiz.objects.get(id = quizid)
    quiz_taker = QuizTaker.objects.filter(user = request.user, quiz = quiz)[0]
    quiz_taker.completed = True
    quiz_taker.save()
    res = False
    if(quiz_taker.completed):
        res = True
    data = {}
    data['totalScore'] = quiz.quizScore
    data['obtainedScore'] = quiz_taker.score
    return JsonResponse({"data":data},safe=True)


@csrf_exempt
def getQuiz(request,quizId):
    user = request.user
    # quizid = request.GET.get('quizId')
    quiz = Quiz.objects.get(id = quizId)
    
    quiz_taker = QuizTaker.objects.filter(user = user, quiz = quiz)
    new_quiz = {}
    
    new_quiz['quiz'] = {}
    new_quiz['quiz']['id'] = quiz.pk
    new_quiz['quiz']['name'] = quiz.name
    new_quiz['quiz']['numberofquestions'] = quiz.numberOfQuestions

    if len(quiz_taker) == 0:
        new_quiz['completed'] = False
    else:
        quiz_taker = quiz_taker[0]
        new_quiz['obtainedScore'] = quiz_taker.score
        new_quiz['totalScore'] = quiz.quizScore
        new_quiz['completed'] = True if quiz_taker.completed == True else False
    
    return JsonResponse({"data": new_quiz},safe=True)