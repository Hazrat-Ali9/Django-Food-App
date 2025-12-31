"""
URL configuration for food_zone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import search_feature,pro_detials,dicout_page
urlpatterns = [
    path('search/', search_feature,name='search_feature'),
    path('dicout_page/', dicout_page,name='dicout_page'),
    path('pro_detials/<int:pk>/', pro_detials,name='pro_detials'),
   

   ]
