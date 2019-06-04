from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth import login, authenticate, logout
from . import forms
from . import models


def home(request):

    return render(request, "home.html")
# Create your views here.


def about(request):
    return render(request, "about.html")


class LoginBasicView(LoginView):
    template_name = './login.html'
    success_url = '/profile'
    next = '/profile'


def logout_view(request):
    logout(request)
    return redirect('/')


def my_profile(request):
    return render(request, "user_my_profile_page.html")


def team(request):
    return render(request, "team.html")


def my_profile_overview(request):
    if(request.user.is_staff):
        return
    else:
        print(User.objects.all().filter(id=request.user.id))

    context = {
        "username": request.user.first_name,
        "email": request.user.email

        }
    return render(request, "my_profile_overview.html", context)


def business_signup(request):
    if request.method == 'POST':
        form = forms.BussinessSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/')
    else:
        form = forms.BussinessSignUpForm()
    return render(request, 'users_register.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = forms.StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/')
    else:
        form = forms.StudentSignUpForm()
    return render(request, 'users_register.html', {'form': form})


def all_courses(request):
    if request.method == 'GET':
        return render(request, 'courses.html', {'courses': models.Course.objects.all()})


@login_required
def my_courses(request):
    if request.method == 'GET':
        cur_user = request.user
        if cur_user.is_staff:
            courses = models.Course.objects.all().select_related(
                'company_provider').filter(company_provider__user=cur_user.pk)
        else:
            enrollment = models.Enrollment.objects.all().select_related(
                'student', 'course').filter(student__user=cur_user.pk).values()
            courses = list(enrollment)
            values = [course['course_id'] for course in courses]
            courses = [models.Course.objects.get(pk=enroll_id) for enroll_id in values]
            print(list(courses))
        return render(request, 'my_profile_courses.html', {'courses': courses})
    return HttpResponse(status=404)


class AddCourseView(CreateView):
    model = models.Course
    fields = '__all__'
    template_name = 'addcourse.html'
    success_url = '/profile'


def course_details(request, course_id):
    if list(models.Enrollment.objects.all().select_related('student').filter(student__user=request.user.id)) == []:
        enrolled = False
    else:
        enrolled = True
    if request.method == 'POST':
        if enrolled == False:
            student = models.Student.objects.get(user=request.user.id)
            course = models.Course.objects.get(id=course_id)
            newly_enrolled = models.Enrollment(student=student, course=course)
            newly_enrolled.save()
            enrolled = True
    course = models.Course.objects.get(id=course_id)
    try:
        content = models.CourseMaterials.objects.all().filter(course=course).values()[0]

    except IndexError:
        content = models.CourseMaterials(course=course)
        content.save()
        content = content.__dict__

    return render(request, 'course.html', {'course': course, 'enrolled': enrolled, 'content': content})


@login_required
def add_content(request, course_id):
    if request.method == 'POST':
        if list(models.Course.objects.all().select_related('company_provider').filter(id=course_id, company_provider__user=request.user)) != []:
            
            content = models.CourseMaterials.objects.get(course=models.Course.objects.get(pk=course_id))
            form = forms.CourseContentForm(request.POST,instance=content)
            if form.is_valid():
                form.course = models.Course.objects.all().filter(id=course_id)[0]
                form.save()

                return redirect('/courses/' + str(course_id))
        else:
            return HttpResponse(status=404)
    else:
        form = forms.CourseContentForm()
    return render(request, 'content.html', {'form': form})
