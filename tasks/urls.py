
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreate.as_view(), name = 'tasks-list'),
]

