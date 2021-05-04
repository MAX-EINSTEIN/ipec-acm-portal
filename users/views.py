from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse_lazy
from .forms import EmailUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import Member

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL))
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = EmailUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


class EditMemberDetails(UpdateView):
    model = Member
    template_name = "users/edit_profile.html"
    fields = ('name', 'roll_no', 'branch', 'year', 'section', 'college_email_id', 'contact_number', 'profile_image', 'experience', 'projects')
    success_url = reverse_lazy('users:dashboard')

