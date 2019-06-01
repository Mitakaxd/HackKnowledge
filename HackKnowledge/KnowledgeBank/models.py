from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=100, blank=True)
    years = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True, blank=True)



class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.TextField(max_length=30, blank=True)
    projects = models.TextField(max_length=500, blank=True)
    begin_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(null=True,blank=True)


class Course(models.Model):
    name = models.TextField(max_length=100, blank=True)
    company_provider = models.ForeignKey(Business, on_delete=models.CASCADE)
    starting_date = models.DateTimeField(null=False,blank=True)
    end_time = models.DateTimeField(null=False,blank=True)
    subject = models.TextField(max_length=60,blank=False)
    description = models.TextField(max_length=500,blank=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Grades(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    weekone = models.IntegerField(null=True, blank=True)
    weektwo = models.IntegerField(null=True, blank=True)
    weekthree = models.IntegerField(null=True, blank=True)
    weekfour = models.IntegerField(null=True, blank=True)
    weekfive = models.IntegerField(null=True, blank=True)
    weeksix = models.IntegerField(null=True, blank=True)
    weekseven = models.IntegerField(null=True, blank=True)
    weekeight = models.IntegerField(null=True, blank=True)
    weeknine = models.IntegerField(null=True, blank=True)
    weekten = models.IntegerField(null=True, blank=True)