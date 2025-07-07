from django.shortcuts import render
from .models import Course
from django.http import HttpResponse
from django.core.management import call_command

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations run successfully.")
    
