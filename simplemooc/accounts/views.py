from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from simplemooc.core.utils import generate_hash_key


# Create your views here.

User = get_user_model()

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
    
def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context={}
    form = PasswordResetForm(request.POST or None) # para nao ser validado logo que acessar/ mostar a mensagem de campo obrigatório
    if form.is_valid():
        user = User.objects.get(email=form.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        context['success'] = True
    context ['form'] = form
    return render(request, template_name, context)#mostra os campos


def password_reset_confirm(request,key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data = request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    return render(request, template_name,context)


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