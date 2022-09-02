from ast import Try
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.
def index(request):
    assets = ["Điện thoại","PC","Laptop"]
    cname = "con gà Đức"
    context = {'name':cname,'assets':assets}
    return render(request,"polls/index.html",context)

def viewlist(request):
    list_question = Question.objects.all()
    # list_question = get_object_or_404(Question,pk=2)
    context = {"dsquest":list_question}
    return render(request,"polls/question_list.html",context)

def detailView(request,question_id):
    q = Question.objects.get(pk=question_id)
    context = {"qs":q}
    return render(request,"polls/detail_question.html",context)

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        catched_data = request.POST["choice"]
        a = q.choice_set.get(pk=catched_data)
        
    except:
        return HttpResponse("Lỗi không có choice")
    a.vote = a.vote + 1
    a.save()
    context = {"q":q}
    return render(request,"polls/result.html",context)