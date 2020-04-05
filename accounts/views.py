from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from products.models import *

# Create your views here.
def register(request):
    print(request.method)
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                if user is None:
                    print("authenticate work")
                else:
                    print("Not Worked")
                user.save()
                print('success full')
                return redirect('login')
        else:
            print("not match")
            messages.info(request,'Password not matching')
            return redirect('register')

    else:
        return render(request,'registration/register.html')

def success(request):
    return render(request,'registration/success.html')

def homepage(request):
    return render(request,'accounts/homepage.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        context={
            'user':user
        }
        if user is not None:
            auth.login(request,user) 
            return redirect('homepage_log',username)
            
        else:
            messages.info(request,'invalid credentials')
            return render(request,'registration/login.html')

    return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')