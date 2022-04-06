from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task, name='task'),
    path('tasks/task-1/', views.task_1, name='task-1'),
]