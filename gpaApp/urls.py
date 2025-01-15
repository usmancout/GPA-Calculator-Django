from django.urls import path
from . import views

urlpatterns = [
    path('', views.gpa_calculator, name='gpa_calculator'),
]
