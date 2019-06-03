from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.TextField(blank=True)
    def __str__(self):
        return self.user.full_name

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, blank=True)
    projects = models.TextField(max_length=500, blank=True)
    begin_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.company_name

class Course(models.Model):
    name = models.CharField(max_length=100, blank=True,unique=True)
    company_provider = models.ForeignKey(Business, on_delete=models.CASCADE)
    starting_date = models.DateTimeField(null=False, blank=True)
    subject = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CourseMaterials(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_one = models.TextField()
    week_two = models.TextField()
    week_three = models.TextField()
    week_four = models.TextField()
    week_five = models.TextField()
    week_six = models.TextField()
    week_seven = models.TextField()
    week_eight = models.TextField()
    week_nine = models.TextField()
    week_ten = models.TextField()

class CourseTests(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_one_test = models.TextField()
    week_two_test = models.TextField()
    week_three_test = models.TextField()
    week_four_test = models.TextField()
    week_five_test = models.TextField()
    week_six_test = models.TextField()
    week_seven_test = models.TextField()
    week_eight_test = models.TextField()
    week_nine_test = models.TextField()
    week_ten_test = models.TextField()


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
