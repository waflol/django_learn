from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title
    
class MyUser(AbstractUser):
    gender_choice = ((0,'Female'),(1,'Male'),(2,'others'))
    age = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    gender = models.IntegerField(choices=gender_choice,default=0)
    address = models.CharField(default='',max_length=255,blank=True)
    