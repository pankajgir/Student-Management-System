from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def courses(request):
    return render(request,'courses.html')

def dashboard(request):
    return render(request,'dashboard.html')  

def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def signup(request):
    return render(request,'sign-up.html')

def create_user(request):
    if request.method =='POST':
        name= request.POST['name']
        email= request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse('email alrady exists')
        else:
             User.objects.create(name=name,email=email,password=password)
             return redirect('/')


def viewstudents(request):
    return render(request,'viewstudents.html')
