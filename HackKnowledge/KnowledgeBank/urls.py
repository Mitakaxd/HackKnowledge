from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'Knowledge_Bank-home'),
    path('about/',views.about,name = 'Knowledge_Bank-about'),
    path('login/',views.LoginBasicView.as_view(), name = "Knowledge_Bank-register_users"),
    path('team/',views.team,name = 'Knowledge_Bank-team'),
    path('register/student/',views.student_signup,name = 'Knowledge_Bank-register'),	
    path('register/business/',views.business_signup,name = 'Knowledge_Bank-register')
]
