from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login



# Create your views here.

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)#cria novos usuarios
        if form.is_valid():
            user = form.save()
            user = authenticate( #faz autenticação depois do cadastro| usuario já fica logado
                username = user.username, password = form.cleaned_data['password1']
            )
            login (request, user) #colocará o usuario na sessao
            return redirect(settings.LOGIN_URL) #faz redirecionamento para a page de login
            
    else:
        form = RegisterForm()
              
    context = {
        'form':form
    }
    return render(request, template_name, context)