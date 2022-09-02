from dataclasses import field
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','time_created',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'titleMF'}),
            'content': forms.Textarea(attrs={'class':'contentMF'}),
        } 
        
class SendEmail(forms.Form):
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'titleUF'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'contentUF','id':'noidung'}))
    cc = forms.BooleanField(required=False)
    