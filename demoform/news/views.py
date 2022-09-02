from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import is_valid_path
from .forms import PostForm,SendEmail
from django.views import View
# Create your views here.
class IndexClass(View):
    def get(self,request):
        return HttpResponse("xin chào")
    
# def index(request):
#     return HttpResponse("xin chào")

# def add_post(request):
#     a = PostForm()
#     context ={'f':a}
#     return render(request,'news/add_news.html',context)

# class PostClass(View):
#     def get(self, request):
#         a = PostForm()
#         context ={'f':a}
#         return render(request,'news/add_news.html',context)

class SaveNewsClass(View):
    def put(self,request):
        pass
    def get(self, request):
        a = PostForm()
        context ={'f':a}
        return render(request,'news/add_news.html',context)
    def post(self,request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("luu oke")
        else:
            return HttpResponse("khong dc validate")

# def save_news(request):
#     if request.method == 'POST':
#         g = PostForm(request.POST)
#         if g.is_valid():
#             g.save()
#             return HttpResponse("luu oke")
#         else:
#             return HttpResponse("khong dc validate")
#     else:
#         return HttpResponse("ko phai post request")
    

def email_view(request):
    b = SendEmail()
    context = {'f':b}
    return render(request,'news/email.html',context)

def process_email(request):
    if request.method == 'POST':
        m = SendEmail(request.POST)
        if m.is_valid():
            # title = m.cleaned_data['title']
            # cc = m.cleaned_data['cc']
            # content = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context = {
            #     'title':title,
            #     'cc' : cc,
            #     'content':content,
            #     'email':email
            # }
            # return render(request,'news/print_email.html',context)
            context2 = {'email_data':m}
            return render(request,'news/print_email.html',context2)
            
        else:
            return HttpResponse('404Error!')
    else:
            return HttpResponse('It is not POST method')