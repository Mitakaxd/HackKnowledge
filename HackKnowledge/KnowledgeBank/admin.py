# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Business)

admin.site.register(models.Course)
admin.site.register(models.CourseMaterials)
admin.site.register(models.CourseTests)
admin.site.register(models.Grades)

