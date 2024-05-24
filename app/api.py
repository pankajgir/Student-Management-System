from .models import *
from rest_framework import generics
from .serializer import Userserializer,courseserializer,studentserializer

class Userapi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class updateuserapi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class deleteuserapi(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class courseapi(generics.CreateAPIView):
    queryset = course.objects.all()
    serializer_class = courseserializer

class updatecourseapi(generics.RetrieveUpdateAPIView):
    queryset = course.objects.all()
    serializer_class = courseserializer


class deletecourseapi(generics.DestroyAPIView):
    queryset = course.objects.all()
    serializer_class = courseserializer


class studentapi(generics.CreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer

class updatestudentapi(generics.RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer


class deletestudentapi(generics.DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer







