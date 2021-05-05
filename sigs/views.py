from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import SpecialInterestGroup

# Create your views here.
def sig_home(request, name):
    name = name.lower()
    sig = get_object_or_404(SpecialInterestGroup, name=name)
    return render(request, 'sigs/home.html', {'sig':sig})


@login_required(login_url=settings.LOGIN_URL)
def tasks_list(request, name):
    name = name.lower()
    sig = get_object_or_404(SpecialInterestGroup, name=name)

    return render(request, 'sigs/tasks_list.html', {'sig':sig})
