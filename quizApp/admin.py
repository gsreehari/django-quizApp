from django.contrib import admin

from .models import Quiz, Question, Answer, QuizTaker


class AnswerInline(admin.TabularInline):
    model = Answer
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]



admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(QuizTaker)
# admin.site.register(Result)
