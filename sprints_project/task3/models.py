from django.db import models

# Create your models here.
class student(models.Model):
    f_name = models.CharField(max_length=255,null=True)
    l_name = models.CharField(max_length=255,null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)

class courses(models.Model):
    current_courses = models.CharField(max_length=255,null=True)
    finished_courses =models.CharField(max_length=255,null=True)