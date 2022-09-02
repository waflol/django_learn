from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.
class IndexClass(View):
    def get(self,request):
        return HttpResponse('<h1>Index</h1>')
    
class LoginClass(View):
    def get(self,request):
        return render(request,'Login/login.html')
    def post(self,request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('User khong ton tai')
        login(request,my_user)
        return render(request,'Login/success.html')
    
class ViewUser(LoginRequiredMixin,View):
    login_url='/login/login'
    def get(self,request):
        return HttpResponse('Day la ViewUSer')
    def post(self,request):
        pass

@decorators.login_required(login_url='/login/login')      
def view_product(request):
    return HttpResponse('Xem san pham')

class AddPost(LoginRequiredMixin,View):
    login_url='/login/login'
    def get(self,request):
        f = PostForm()
        context = {'form':f}
        return render(request,'Login/addpost.html',context)
        
    def post(self,request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('wrong data')
        
        print(request.user.get_all_permissions())
        # cache reload từ database user 
        if request.user.has_perm('Login.add_post'):
            f.save()
        else:
            return HttpResponse('K co quyen')
        return HttpResponse('ok')