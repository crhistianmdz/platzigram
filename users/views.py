#django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
#exceptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from . import models

#forms

from users.forms import ProfileForm
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

def update_profile_view(request):
    profile=request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            
            profile.website=data['website']
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()
            return redirect('update_profile_view')
    else:
        form=ProfileForm()
    return render(
            request=request, 
            template_name='users/update_profile.html',
            context={
                'profile':profile,
                'user':request.user,
                'form': form
            }
        )