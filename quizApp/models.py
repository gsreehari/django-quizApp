from django.db import models
from django.contrib.auth.models import User

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    numberOfQuestions = models.IntegerField(default=10)
    quizScore = models.FloatField(default=10)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'quizes'

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question.all()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="question")
    label = models.CharField(max_length=1000)
    questionDifficulty = models.CharField(max_length=100, choices=DIFF_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    questionMarks = models.IntegerField(default=1)

    def __str__(self):
        return self.label

    def get_answers(self):
        return self.answer.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="answer")
    label = models.CharField(max_length=100)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username
