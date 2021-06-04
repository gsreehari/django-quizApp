
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # backend api

    path('api/signup',views.signup,name="quizApp-signup"),
    path('api/signin',views.signin,name="quizApp-signin"),
    path('api/signout',views.signout,name="quizApp-signout"),
    path('api/checkAnswer',views.checkAnswer),
    path('api/quizAttempted',views.quizAttempted),
    path('api/getQuiz/<int:quizId>',views.getQuiz),


    # frontend 
    path('signup',views.signupPage),
    path('signin',views.signinPage),
    path('home', views.home,name="quizApp-home"),
    path('admin/', admin.site.urls),
    path('', views.signinPage),
    path('quiz/<int:quizId>', views.quizPage),


]