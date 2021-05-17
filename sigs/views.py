from tasks.models import Task
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.utils import timezone as tz
from django.contrib.auth.decorators import login_required
from .models import SpecialInterestGroup


# Create your views here.
def sig_home(request, name):
    name = name.lower()

    sigs = []
    if request.user.is_anonymous:
        sigs_joined = 0
    else:
        sigs = request.user.member.sigs.all()
        sigs_joined = len(sigs)

    sig = get_object_or_404(SpecialInterestGroup, name=name)

    context = {'sig': sig, 'sigs_joined': sigs_joined, 'is_member': False}

    if sig in sigs:
        context['is_member'] = True
        return render(request, 'sigs/home.html', context=context)

    return render(request, 'sigs/home.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def sig_tasks(request, name):
    name = name.lower()
    sig = get_object_or_404(SpecialInterestGroup, name=name)

    title = f'SIG {sig.name} TASKS'.upper()
    tasks = Task.objects.filter(sig=sig)
    submitted_tasks = tasks.filter(
        task_submission__submitted_by=request.user.member)
    now = tz.now()

    context = {
                'title': title,
                'tasks': tasks.all(), 
                'submitted_tasks': submitted_tasks, 
                'now': now
            }

    if sig in request.user.member.sigs.all():
        return render(request, 'components/tasks_list.html', context)
    return redirect('sigs:home', slug=sig.name)
