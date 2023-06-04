from django.urls import path
from .views import *
urlpatterns=[
    path('',main_drf),
    path('tasks/',TaskListView.as_view()),
    path('tasks/create/',TaskCreateView.as_view()),
    path('tasks/<int:pk>/',GetTaskView.as_view()),
    path('tasks/<int:pk>/delete/',TaskDeleteView.as_view()),
    path('tasks/<int:pk>/update/',TaskPutView.as_view()),
]