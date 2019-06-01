from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'Knowledge_Bank-home'),
    path('about/',views.about,name = 'Knowledge_Bank-about'),
    path('login/',views.LoginBusinessView.as_view(), name = "Knowledge_Bank-register_users")
]
