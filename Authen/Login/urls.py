"""Authen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import IndexClass,LoginClass,ViewUser, view_product, AddPost
app_name = 'Login'
urlpatterns = [
    path('', IndexClass.as_view(),name='index'),
    path('login/',LoginClass.as_view(),name='login'),
    path('user-view/',ViewUser.as_view(),name='viewuser'),
    path('product-view/',view_product,name='view_product'),
    path('addpost/',AddPost.as_view(),name='addpost')
]
