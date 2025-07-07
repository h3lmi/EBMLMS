from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse

def course_list(request):
    from .models import Course
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def run_migrations(request):
    try:
        call_command('migrate', interactive=False)
        return HttpResponse("✅ Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Migration error: {e}")


