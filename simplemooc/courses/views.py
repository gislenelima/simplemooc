from django.shortcuts import render, get_object_or_404, redirect
from simplemooc.courses.models import Course
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment
from .forms import ContactCourse

# Create  your views here.

def index(request):
    courses = Course.objects.all()
    return render(request,'courses/index.html', {'courses':courses})


def details(request, slug): #descrição do curso
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method =='POST':
        form = ContactCourse(request.POST)
        if form.is_valid():   #verifica validação
            context['is_valid'] = True
            form.send_mail(course) 
            form = ContactCourse()
            
    else: 
        form = ContactCourse()
    context['form'] = form 
    context['course'] = course
    template_name = 'courses/details.html'
    return render (request, template_name, context)
    
@login_required    
def enrollment(request, slug):
    course = get_object_or_404(Course, slug = slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user = request.user, course = course
    )
    # if created: 
    #     enrollment.active()
    return redirect('dashboard')
