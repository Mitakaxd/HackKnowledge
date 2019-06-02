from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from . import models

def home(request):
    
    return render(request,"home.html")
# Create your views here.
    

def about(request):
    return render(request,"about.html")

class LoginBusinessView(LoginView):
	template_name = './login.html'


def team(request):
    return render(request,"team.html")



def users_register(request):
    return render(request,"users_register.html")