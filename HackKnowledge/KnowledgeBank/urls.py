from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'Knowledge_Bank-home'),
    path('about/',views.about,name = 'Knowledge_Bank-about'),
    path('login/',views.LoginBusinessView.as_view(), name = "Knowledge_Bank-register_users"),
    path('team/',views.team,name = 'Knowledge_Bank-team'),
    path('users_register/',views.users_register,name = 'Knowledge_Bank-register')
]
