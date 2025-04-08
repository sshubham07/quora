from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recent/', views.recent_questions, name='recent_questions'),
]
