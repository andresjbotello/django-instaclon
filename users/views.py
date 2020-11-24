# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm


def update_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.biography = data["biography"]
            profile.picture = data["picture"]

            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()
    
    return render(request,"users/update_profile.html",{'profile':profile,
                                                        'user':request.user,
                                                        'form':form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect("feed")
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})
    return render(request,'users/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']
        pwd_confirm = request.POST['password_confirm']

        if pwd != pwd_confirm:
            return render(request,'users/signup.html',{"error":"Passwords must be equals!"})
        
        try:
            user = User.objects.create_user(username=username,password=pwd)
        except IntegrityError:
            return render(request,'users/signup.html',{'error':'Username is already in use'})
        

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

        
    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')