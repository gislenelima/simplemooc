from simplemooc.courses import views
from django.contrib import admin
from django.urls import path, include
from simplemooc.courses import views 

urlpatterns = [
    path('', views.index, name = 'index')
   
    
]