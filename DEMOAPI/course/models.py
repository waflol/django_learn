from turtle import title
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title