from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
]
