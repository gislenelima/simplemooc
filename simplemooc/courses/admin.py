from django.contrib import admin

# Register your models here.

from .models import Course #importa models que vai querer cadastrar

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date','created_at'] 
    search_fields = ['name','slug']

    
admin.site.register(Course, CourseAdmin)