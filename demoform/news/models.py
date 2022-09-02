from pyexpat import model
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    content = models.TextField(max_length=1000,blank=False,null=False)
    time_created = models.DateTimeField(default=timezone.datetime.now())
    
    def __str__(self) -> str:
        return self.title
    
