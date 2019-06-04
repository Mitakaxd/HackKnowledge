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
    path('register/business/',views.business_signup,name = 'regbusiness'),
    path('profile/',views.my_profile,name = "profile"),
    path('mycourses/', views.my_courses, name='mycourses'),
    path('addcourse/',views.AddCourseView.as_view(),name='addcourse'),
    path('courses/<int:course_id>', views.course_details,name='course'),
    path('courses/<int:course_id>/addcontent', views.add_content,name='addcontent')

    ]
