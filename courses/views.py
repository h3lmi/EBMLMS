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


def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        return HttpResponse("✅ Superuser created: admin / adminpass123")
    else:
        return HttpResponse("ℹ️ Superuser 'admin' already exists.")
