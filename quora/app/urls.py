from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recent/', views.recent_questions, name='recent_questions'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),


]
