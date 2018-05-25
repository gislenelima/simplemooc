from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL) #faz redirecionamento para a page de login
            
    else:
        form = UserCreationForm()
              
    context = {
        'form':form
    }
    return render(request, template_name, context)