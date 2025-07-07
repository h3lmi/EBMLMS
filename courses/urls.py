from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # will be at /courses/
    path('run-migrations/', views.run_migrations),  # temporary route
]
