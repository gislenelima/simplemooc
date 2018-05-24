from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactCourse(forms.Form):

    name = forms.CharField(label = 'Nome', max_length=100)
    email = forms.EmailField(label = 'E-mail')
    message = forms.CharField(label = 'Mesagem/Dúvida', widget = forms.Textarea)


#regras de negicio sempre deixar por aqui

    def send_mail(self, course):
        subject = '[%s] Contato' % course 
        message = 'Nome: %(name)s; E-mail:%(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            
        }

        template_name = 'courses/contact_email.html'
        send_mail(
            subject, message, settings.DEFAULT_FROM_EMAIL, 
        [settings.CONTACT_EMAIL]
        )



