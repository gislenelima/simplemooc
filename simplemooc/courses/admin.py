from django.contrib import admin

# Register your models here.

from .models import Course #importa models que vai querer cadastrar

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date'] 
    search_fields = ['name','slug']
    prepopulated_fields = {'slug':('name',)} #popula o campo slug no cadastro do fórmulario

    
admin.site.register(Course, CourseAdmin)