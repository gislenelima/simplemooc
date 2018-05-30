from simplemooc.courses import views
from django.contrib import admin
from django.urls import path, include
from simplemooc.courses import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug>/detail', views.details, name='details'),
    path('<slug>/inscricao', views.enrollment, name='enrollment'),
] 