from django.urls import path,include
from django.conf.urls import url
from simplemooc.accounts import views
from django.contrib.auth.views import login


urlpatterns = [
    path('entrar/',login, {'template_name':'accounts/login.html'}, name = 'login'),
    path('cadastre-se/',views.register, name = 'register'),
]

