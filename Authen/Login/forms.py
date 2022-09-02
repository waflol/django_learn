from pyexpat import model
from django.forms import ModelForm
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = {'title','content'}
    