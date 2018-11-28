from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendees, name='attendees'),
] 