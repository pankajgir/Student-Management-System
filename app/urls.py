"""
URL configuration for student_panle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static
from.api import *

urlpatterns = [
    path('',index),
    path('signin/',signin),
    path('registration/',create_user),
    path('courses/',courses),
    path("delete/<int:pk>",delete_course,name='delete'),
    path("delete_student/<int:pk>/",delete_student, name='delete_student'),
    path("updatecourse/<int:uid>/",updatecourse, name="updatecourse"),
    path('dashboard/',dashboard),
    path("profile/<int:pk>/",profile ,name='profile'),
    path('signup/',signup),
    path('viewstudents/',viewstudents),
    path('course_registration/',course_registration),
    path('add_student/', add_student),
    path('update_course/',update_course),
    path('update_student/',update_student),
    path("search/",search,name='search'),
    path("updatestudent/<int:uid>/",updatestudent, name="updatestudent"),

    # This is Api Url
    path("api/user/",Userapi.as_view()),
    path("api/updateuserapi/<int:pk>/",updateuserapi.as_view()),
    path("api/deleteuserapi/<int:pk>/",deleteuserapi.as_view()),
    path("api/course/",courseapi.as_view()),
    path("api/updatecourseapi/<int:pk>/",updatecourseapi.as_view()),
    path("api/deletecourseapi/<int:pk>/",deletecourseapi.as_view()),
     path("api/student/",studentapi.as_view()),
    path("api/updatestudentapi/<int:pk>/",updatestudentapi.as_view()),
    path("api/deletestudentapi/<int:pk>/",deletestudentapi.as_view()),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
