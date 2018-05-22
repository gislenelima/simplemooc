from django.contrib import admin

# Register your models here.

from .models import Course #importa models que vai querer cadastrar

admin.site.register(Course)