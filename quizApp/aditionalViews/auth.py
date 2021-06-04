from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def authSignup(username,password):
    if username != None and username != "":
        if password != None and password != "":
            user = User.objects.create_user(username, '', password)
            return {"code":"SUS","message":"user added"}
        else:
            return {"code":"EP","message":"password required"}
    
    return {"code":"EU","message":"username required"}


def authSignin(username,password,request):
    if username != None and username != "":
        if password != None and password != "":
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return {"code":"SIS","message":"user authenticated"}
            else:
                return {"code":"SIUS","message":"invalid credentials"}
        else:
            return {"code":"EP","message":"password required"}
    
    return {"code":"EU","message":"username required"}


def authSignOut(request):
    logout(request)
    return {"code":"SOS","message":"Sign out success"}