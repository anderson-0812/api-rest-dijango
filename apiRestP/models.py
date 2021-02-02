from django.db import models

# Create your models here.
class User(models.Model):
    ci = models.CharField(max_length=10)
    name =  models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    phone =  models.CharField(max_length=10)
    email =  models.CharField(max_length=50)
    address =  models.CharField(max_length=100)
