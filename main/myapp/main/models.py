from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from traitlets import default
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    labname = models.CharField(max_length=100, blank= True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self) -> str:
        return self.user.username

class patientregistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    lastname= models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    address= models.CharField(max_length=100, blank=True)
    age = models.IntegerField(default=0)
    email= models.CharField(max_length=100, blank=True)
    mobile = models.IntegerField(default=0)
    dateofbirth= models.IntegerField(default=0)
    passport = models.IntegerField(default=0)
    pannumber= models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return self.user.username
    

