from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'home'),
    path('about/',views.about,name = 'about'),
    path('login/',views.LoginBasicView.as_view(), name = "login"),
    path('courses/',views.all_courses, name='courses'),
    path('logout/',views.logout_view, name = "logout"),
    path('team/',views.team,name = 'team'),
    path('register/student/',views.student_signup,name = 'regstudent'),	
    path('register/business/',views.business_signup,name = 'regbusiness')
    #path('mycourses/', views.my_courses, name='mycourses'),
    #path('addcourse/',views.addcourse,name='addcourse')
    ]
