from django.db import models

# Create your models here.
class info(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    mobile = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)