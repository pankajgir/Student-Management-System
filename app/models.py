from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)

class course(models.Model):
    course_name=models.CharField(max_length=250)
    fees=models.IntegerField()
    duration=models.CharField(max_length=50)

class student(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    mobile_no=models.IntegerField()
    college=models.CharField(max_length=250)
    degree=models.CharField(max_length=250)
    address=models.TextField()
    image=models.FileField(upload_to='profile',max_length=100)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
class person(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)