from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),                 # Получение списка всех задач
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),      # Создание новой задачи
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),   # Получение деталей задачи по ID
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),  # Обновление задачи
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),  # Удаление задачи
]
