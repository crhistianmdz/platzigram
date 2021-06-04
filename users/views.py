from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from . import models
# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        passwordConfirm=request.POST['confirm_password']
        firstName=request.POST['first_name']
        lastName=request.POST['last_name']
        email=request.POST['email']
        if password != passwordConfirm:
            return render(request,'users/signup.html',{'error':'Password confirmation no match'})
        try:
            user=User.objects.create_user(username=username, email=email, password=password)
        except IntegrityError:
            return render(request,'users/signup.html',{'error':'Username is already in user'})
        user.last_name=lastName
        user.firs_tname=firstName
        user.save()
        profile=models.Profile(user=user)
        profile.save()
        return redirect('login_view')

    return render(request,'users/signup.html')