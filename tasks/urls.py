# urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('api/tasks/', views.api_tasks, name='api_tasks'),
]
