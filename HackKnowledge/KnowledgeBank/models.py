from django.db import models


class BaseUser(models.Model):
    user_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    full_name = models.TextField()
    email = models.TextField()
    are_you_business = models.BooleanField()
    date_of_birth = models.DateTimeField()

class User(models.Model):
    pass
# Create your models here.



class Business(models.Model):
    pass


class Course(models.Model):
    name = models.TextField()
    company_provider = models.TextField()
    starting_date = models.DateTimeField()
    end_time = models.DateTimeField()
    subject = models.TextField()