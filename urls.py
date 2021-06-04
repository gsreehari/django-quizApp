"""quizApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/checkAnswer',views.checkAnswer),
    path('api/signup',views.signup,name="quizApp-signup"),
    path('api/signin',views.signin,name="quizApp-signin"),


    # frontend 
    path('signup',views.signupPage),
    path('signin',views.signinPage),
    path('home', views.home,name="quizApp-home"),
    path('admin/', admin.site.urls),
    path('', views.signinPage),
    path('quiz/<int:quizId>', views.quizPage),

]
