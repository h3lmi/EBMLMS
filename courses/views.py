from django.shortcuts import render
from .models import Course

def course_list(request):
    print("🌀 This view has been updated.")  # ✅ Add this line here
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
