from django.urls import path, include
from .views import register, dashboard, EditMemberDetails, sigs_joined, member_tasks

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/register/', register, name='register'),
    path('users/dashboard/', dashboard, name='dashboard'),
    path('users/edit-profile/<slug:pk>/', EditMemberDetails.as_view(),  name='edit-profile'),
    path('users/sigs-joined/', sigs_joined, name='sigs_joined'),
    path('users/member-tasks/', member_tasks, name='member_tasks'),
]