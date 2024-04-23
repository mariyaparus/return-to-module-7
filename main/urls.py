from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, view_student

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', view_student, name='view_student')
]