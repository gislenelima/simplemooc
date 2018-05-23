from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course

# Create  your views here.

def index(request):
    courses = Course.objects.all()
    return render(request,'courses/index.html', {'courses':courses})


def details(request, slug):
    course = get_object_or_404(Course,slug=slug)
    return render (request, 'courses/details.html',{'course':course})

