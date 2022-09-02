from turtle import title
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer
# Create your views here.

class GetAllCourseAPIView(APIView):
    def get(self,request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course,many=True)
        return Response(data=mydata.data,status=status.HTTP_200_OK)

    def post(self,request):
        mydata = CourseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Sai data',status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['title1']
        price = mydata.data['price1']
        content = mydata.data['content1']
        cs = Course.objects.create(title=title,price=price,content=content)
        return Response(data=cs.id,status=status.HTTP_200_OK)