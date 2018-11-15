from django.views import generic
from .models import Semester_1,Semester_2,Semester_3,Semester_4,Semester_5,Semester_6,Semester_7,Semester_8
from django.contrib.auth.decorators import login_required
from .models import Course1_sem1,Course2_sem1,Course3_sem1,Course4_sem1,Course5_sem1,Course1_sem2,Course2_sem2,Course3_sem2,Course4_sem2,Course5_sem2
from .models import Course1_sem3,Course2_sem3,Course3_sem3,Course4_sem3,Course5_sem3,Course1_sem4,Course2_sem4,Course3_sem4,Course4_sem4,Course5_sem4
from .models import Course1_sem5,Course2_sem5,Course3_sem5,Course4_sem5,Course5_sem5,Course1_sem6,Course2_sem6,Course3_sem6,Course4_sem6,Course5_sem6,Course1_sem7,Course2_sem7,Course3_sem7,Course4_sem7,Course5_sem7,Course1_sem8
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
#from .forms import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.core.urlresolvers import reverse_lazy, reverse


class IndexView(generic.ListView):
    template_name = 'recruiter/semester_new.html'


    def get_queryset(self):
        return Semester_1.objects.all()

class CourseView1(generic.ListView):
    model=Semester_1
    template_name='recruiter/Course.html'
    def get_queryset(self):
        return Semester_1.objects.all()



class CourseView2(generic.ListView):
    model=Semester_2
    template_name='recruiter/Course2.html'
    def get_queryset(self):
        return Semester_2.objects.all()


class CourseView3(generic.ListView):
    model=Semester_3
    template_name='recruiter/Course3.html'
    def get_queryset(self):
        return Semester_3.objects.all()


class CourseView4(generic.ListView):
    model=Semester_4
    template_name='recruiter/Course4.html'
    def get_queryset(self):
        return Semester_4.objects.all()

class CourseView5(generic.ListView):
    model=Semester_5
    template_name='recruiter/Course5.html'
    def get_queryset(self):
        return Semester_5.objects.all()

class CourseView6(generic.ListView):
    model=Semester_6
    template_name='recruiter/Course6.html'
    def get_queryset(self):
        return Semester_6.objects.all()


class CourseView7(generic.ListView):
    model=Semester_7
    template_name='recruiter/Course7.html'
    def get_queryset(self):
        return Semester_7.objects.all()

class CourseView8(generic.ListView):
    model=Semester_8
    template_name='recruiter/sem8_courses.html'
    def get_queryset(self):
        return Semester_8.objects.all()

#
# class Sem1_CourseView1(generic.ListView):
#     model=Course1_sem1
#     template_name='recruiter/Sem1_course1.html'
#     def get_queryset(self):
#         return Course1_sem1.objects.all()
#

def Sem1_Course1(request):

    courses  = Course1_sem1.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem1_Course2(request):

    courses  = Course2_sem1.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem1_Course3(request):

    courses  = Course3_sem1.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem1_Course4(request):

    courses  = Course4_sem1.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem1_Course5(request):

    courses  = Course5_sem1.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem2_Course1(request):

    courses  = Course1_sem2.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem2_Course2(request):

    courses  = Course2_sem2.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem2_Course3(request):

    courses  = Course3_sem2.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem2_Course4(request):

    courses  = Course4_sem2.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem2_Course5(request):

    courses  = Course5_sem2.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem3_Course1(request):

    courses  = Course1_sem3.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})

def Sem3_Course2(request):

    courses  = Course2_sem3.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})

def Sem3_Course3(request):

    courses  = Course3_sem3.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem3_Course4(request):

    courses  = Course4_sem3.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem3_Course5(request):

    courses  = Course5_sem3.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem4_Course1(request):

    courses  = Course1_sem4.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})

def Sem4_Course2(request):

    courses  = Course2_sem4.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem4_Course3(request):

    courses  = Course3_sem4.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem4_Course4(request):

    courses  = Course4_sem4.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem4_Course5(request):

    courses  = Course5_sem4.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem5_Course1(request):

    courses  = Course1_sem5.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem5_Course2(request):

    courses  = Course2_sem5.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem5_Course3(request):

    courses  = Course3_sem5.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem5_Course4(request):

    courses  = Course4_sem5.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})

@login_required
def Sem5_Course5(request):

    courses  = Course5_sem5.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem6_Course1(request):

    courses  = Course1_sem6.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem6_Course2(request):

    courses  = Course2_sem6.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem6_Course3(request):

    courses  = Course3_sem6.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem6_Course4(request):

    courses  = Course4_sem6.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})



def Sem6_Course5(request):

    courses  = Course5_sem6.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem7_Course1(request):

    courses  = Course1_sem7.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem7_Course2(request):

    courses  = Course2_sem7.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem7_Course3(request):

    courses  = Course3_sem7.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem7_Course4(request):

    courses  = Course4_sem7.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem7_Course5(request):

    courses  = Course5_sem7.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})


def Sem8_Course1(request):

    courses  = Course1_sem8.objects.all()

    return render(request, 'recruiter/Sem1_course1.html', {'courses': courses})