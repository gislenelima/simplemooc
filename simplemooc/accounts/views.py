from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditAccountForm

# Create your views here.

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)

@login_required
def edit (request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['sucess']= True

    else: 
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request,template_name, context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method =='POST':
       form = PasswordChangeForm(data = request.POST, user = request.user)  #data: parametro dos dados| forma nomeada
       if form.is_valid():
            form.save()
            context['success'] = True
    
    else:
        form = PasswordChangeForm(user = request.user) 
    context['form'] = form 
    return render(request, template_name, context)
    

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