from django.urls import path,include
from django.conf.urls import url
from simplemooc.accounts import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    path('entrar/',login, {'template_name':'accounts/login.html'}, name = 'login'),
    path('cadastre-se/',views.register, name = 'register'),
    path('sair/',logout, {'next_page':'home'}, name = 'logout'),#repassado o link nao a template + o if no home
]

