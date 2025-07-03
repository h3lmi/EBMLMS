from django.template.loader import get_template

def course_list(request):
    from django.http import HttpResponse
    try:
        t = get_template("base.html")
        return HttpResponse("✔️ base.html is found!")
    except Exception as e:
        return HttpResponse(f"❌ base.html not found: {e}")
