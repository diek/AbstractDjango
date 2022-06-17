# student_tracker urls

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home')
]
