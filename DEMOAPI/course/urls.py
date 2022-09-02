from django.urls import path
from course.views import GetAllCourseAPIView
urlpatterns = [
    path('course/',GetAllCourseAPIView.as_view()),
]