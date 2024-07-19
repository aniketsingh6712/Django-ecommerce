from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout

from django.contrib.auth.models import User,auth
from django.contrib import messages
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email= request.POST['email']
        phone = request.POST['phone']
       
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName taken')
                return redirect('/account/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('/account/signup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect('/account/')
        else:
            messages.info(request,'Passwords are not same')
            return redirect('/account/signup')
    else:
        return render(request, 'account/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request,'invalid credentials') 
            return redirect('/account')
    else:
        
        return render(request, 'account/signin.html')


def signout(request):
    
    logout(request)
    return redirect('home')

