from django.db import models


class BaseUser(models.Model):
    user_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    full_name = models.CharField()
    email = models.CharField()
    are_you_business = models.BooleanField()
    date_of_birth = models.DateTimeField()

class User(models):
    pass
# Create your models here.



class Business(models):
    pass


class Course(models):
    name = models.CharField()
    company_provider = models.CharField()
    starting_date = models.DateTimeField()
    end_time = models.DateTimeField()
    subject = models.CharField()