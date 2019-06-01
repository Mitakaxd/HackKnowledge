from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    
    return render(request,"home.html")
# Create your views here.
    

def about(request):
    return render(request,"about.html")

def users_register(request):
    return render(request,"users_register.html")