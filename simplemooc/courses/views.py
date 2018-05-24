from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course
from .forms import ContactCourse


# Create  your views here.

def index(request):
    courses = Course.objects.all()
    return render(request,'courses/index.html', {'courses':courses})


def details(request, slug): #descrição do curso
    course = get_object_or_404(Course, slug=slug)
    context = {'course':course,'form': ContactCourse()}
    template_name = 'courses/details.html'
    return render (request, template_name, context)
    
