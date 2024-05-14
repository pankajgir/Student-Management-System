from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def courses(request):
    return render(request,'courses.html')

def dashboard(request):
    return render(request,'dashboard.html')  

def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method == "POST":
        person=User.objects.get(email=request.POST['email'])
        print(person)
        if check_password(request.POST['password'],person.password):
            request.session['index']=True
            request.session['email']=person.email
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid email and password')
            return redirect('/')

def courses(request):
    course_obj = course.objects.all()
    return render(request,"courses.html", {"course_obj":course_obj})

def profile(request,pk):
    student_obj =student.objects.get(id=pk)
    return render(request,"profile.html" , {"student_obj":student_obj})

def signup(request):
    return render(request,'sign-up.html')

def create_user(request):
    if request.method =='POST':
        name= request.POST['name']
        email= request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
           messages.error(request, "Email already exist")
        else:
             User.objects.create(name=name,email=email,password=password)
             return redirect('/')
def viewstudents(request):
    course_obj = course.objects.all()
    student_obj= student.objects.all()
    return render(request,"viewstudents.html", {"course_obj":course_obj, "student_obj":student_obj })

        
def course_registration(request):
    if request.method =="POST":
        course_name=request.POST["course_name"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        if course.objects.filter(course_name=course_name).exists():
            return HttpResponse("Cousre name already existS")
        else:
            course.objects.create(course_name=course_name,fees=fees,duration=duration)
            return redirect('/courses/')

def delete_course(request,pk):
    course.objects.get(id=pk).delete()
    return redirect('/courses/')

def updatecourse(request,uid):
    update_obj=course.objects.get(id=uid)
    return render(request, "update-course.html", {"update_obj":update_obj})

def update_course(request):
    if request.method =="POST":
        uid = request.POST["uid"]
        course_name=request.POST["course_name"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        course.objects.filter(id=uid).update(course_name=course_name,fees=fees,duration=duration)
        messages.success(request,"User Update Sucessfully")
        return redirect('/courses/')
        
def add_student(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile_no=request.POST.get('mobile_no')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        address=request.POST.get('address')
        image=request.FILES.get('image')
        course_id=request.POST.get('course')
        new_course=course.objects.get(id=course_id)
        if student.objects.filter(email=email).exists():
             messages.error(request , "email already exist")
        elif student.objects.filter(mobile_no=mobile_no).exists():
             messages.error(request , "mobile_no already exist")
        else:
            stu = student.objects.create(name=name,email=email,mobile_no=mobile_no,
                                         college=college,degree=degree,address=address,
                                         image=image,course=new_course)
            messages.success(request, "student add successfully")                         
            return redirect("/viewstudents/")
def delete_student(request,pk):
    student.objects.get(id=pk).delete()
    return redirect('/viewstudents/')
        
def updatestudent(request,uid):
    course_obj = course.objects.all()
    update_obj=student.objects.get(id=uid)
    return render(request, "update-student.html", {"course_obj":course_obj, "update_obj":update_obj})

def update_student(request):
    if request.method =="POST":
        uid = request.POST.get("uid")
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        college = request.POST.get("college")
        degree = request.POST.get("degree")
        address = request.POST.get("address")
        image = request.FILES.get("image")
        course_id = request.POST.get("courses")
        new_course = course.objects.get(id=course_id)
        student.objects.filter(id=uid).update(name=name, email=email, mobile_no=mobile_no, college=college
                                             ,degree=degree, address=address, image=image, courses=new_course)
        messages.success(request,"student Update Sucessfully")
        return redirect('/viewstudents/')
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q)) | Q(mobile_no__icontains=q)
        student_obj = student.objects.filter(multiple_q)
        print(multiple_q)
    else:
        student_obj = student.objects.all()
    context = {'student_obj':student_obj}
    return render(request,'viewstudents.html',context)
    



