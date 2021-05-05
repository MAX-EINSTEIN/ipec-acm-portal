from django.urls import path
from . import views

app_name = 'sigs'

urlpatterns = [
    path('home/<slug:name>/', views.sig_home, name='home'),
    path('tasks/<slug:name>/', views.tasks_list, name='tasks_list')
]