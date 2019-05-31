from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'Knowledge_Bank-home'),
    path('about/',views.about,name = 'Knowledge_Bank-about'),
    path('users-register/',views.users_register, name = "Knowledge_Bank-register_users")
]
