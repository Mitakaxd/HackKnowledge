from django.shortcuts import render,redirect
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
from . import models
from django.contrib.auth import login, authenticate, logout
from . import forms
def home(request):
    
    return render(request,"home.html")
# Create your views here.
    

def about(request):
    return render(request,"about.html")

class LoginBasicView(LoginView):
	template_name = './login.html'

def logout_view(request):
	logout(request)
	return redirect('/')

def my_profile(request):

    return render(request,"user_my_profile_page.html")


def team(request):
    return render(request,"team.html")


def my_profile_overview(request):
    context = {
        "username": {{user.first_name}},
        "email": {{user.email}}    

    }
    return render(request,"my_profile_overview.html",context)
def business_signup(request):
    if request.method == 'POST':
        form = forms.BussinessSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
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
            return redirect('/')
    else:
        form = forms.StudentSignUpForm()
    return render(request, 'users_register.html', {'form': form})

def all_courses(request):
    if request.method=='GET':
        return render(request, 'courses.html', {'courses':models.Course.objects.all()})

# def mycourses(request):
#     if request.method=='GET':
#         return render(request,'mycourses.html', {'courses':models.Enrollment})
#TODO join tables and get only my courses
#TODO check if logged user is staff, join diff tables


#TODO add Course view