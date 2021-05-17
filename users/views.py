from django.forms.widgets import CheckboxSelectMultiple
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone as tz
from .forms import EmailUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.forms.models import modelform_factory
from .models import Member
from tasks.models import Task

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
            return redirect(settings.SIGNUP_REDIRECT_URL, pk=request.user.member.pk)
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = EmailUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


class EditMemberDetails(UpdateView):
    model = Member
    template_name = "users/edit_profile.html"
    my_fields = ('name', 'roll_no', 'bio', 'branch', 'year', 'section', 'college_email_id', 'contact_number', 'profile_image', 'experience', 'projects', 'sigs')
    form_class =  modelform_factory(Member, fields=my_fields,
        widgets={"sigs": CheckboxSelectMultiple })
    success_url = reverse_lazy('users:dashboard')


@login_required(login_url=settings.LOGIN_URL)
def sigs_joined(request):
    return render(request, 'users/sigs_joined.html')


@login_required(login_url=settings.LOGIN_URL)
def member_tasks(request):
    member = request.user.member
    sigs_joined = member.sigs.all()

    title = 'ALL TASKS'

    tasks = []
    submitted_tasks = []

    for sig in sigs_joined:
        tasksRM = Task.objects.filter(sig=sig)
        submitted_tasksRM = tasksRM.filter(task_submission__submitted_by=member)

        tasks += tasksRM.all()
        submitted_tasks += submitted_tasksRM.all()

    now = tz.now()

    context = {
                'title': title,
                'tasks': tasks, 
                'submitted_tasks': submitted_tasks, 
                'now': now,
                'show_sig': True
            }

    return render(request, 'components/tasks_list.html', context)