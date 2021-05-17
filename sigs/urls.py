from django.urls import path
from . import views

app_name = 'sigs'

urlpatterns = [
    path('home/<slug:name>/', views.sig_home, name='home'),
    path('<slug:name>/sig_tasks/', views.sig_tasks, name='sig_tasks')
]