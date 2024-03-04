from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
def home(request):
    s = Men_latest.objects.all
    return render(request,"index.html",{'product':s})

# create a user 
def sign(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['password']
        User.objects.create_user(username=a,email=b,password=c)
        return render(request,"login.html")
    else:
        return render(request,"signup.html")

# lgon through a user
def log_in(request):
    if request.POST =='POST':
        usr_name = request.POST.get['name']
        passwrd = request.POST.get['password']
        usrr = authenticate(username=usr_name, password=passwrd)
        if usrr is not None:
            auth.login(request,usrr)
            return HttpResponse("User login")
        else:
            return HttpResponse("error")
    else:
        return render(request,"login.html")
    
#show data of user
def showing(request):
    s = User.objects.all()
    return render(request,'show.html',{'disp':s})



# def addingg(request): #foregin key
    if request.method == 'POST':
        if Men_latest.objects.get(id=id):
            a = request.POST['price']
            expanding.object.create(price=a)
            return HttpResponse("ok done") 
        else:
            return HttpResponse("OOPS you got an error")

def aboutt(request):
    return render(request,"about.html")

def contactt(request):
    return render(request,"contact.html")

def product(request):
    return render(request,"products.html")

def single(request):
    return render(request,"single-product.html")
