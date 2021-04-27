from django.urls import path, include
from .views import register, dashboard

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/register/', register, name='register'),
    path('users/dashboard/', dashboard, name='dashboard'),
]