from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('details/<int:pk>/', views.TaskDetails.as_view(), name='detail')
]