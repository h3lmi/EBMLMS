from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.course_list, name='course_list'),
#]
urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),  # default homepage
    path('courses/', views.course_list, name='course_list'),
]
