from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import Task
from .forms import TaskSubmissionForm

# Create your views here.
class TaskDetails(DetailView):
    model = Task
    template_name = 'tasks/task_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        form = TaskSubmissionForm(self.request.POST, self.request.FILES)
        context["form"] = form
        context["submitted"] = self.is_submitted()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form:TaskSubmissionForm = self.get_context_data()['form']
        if form.is_valid():
            submission = form.save(False)
            submission.submitted_by = self.request.user.member
            submission.submitted_for = self.object
            form.save()
            return redirect('sigs:tasks_list', name=self.object.sig.name)
        return self.post(request, *args, **kwargs)


    def is_submitted(self) -> bool:
        subs = self.object.task_submission.all()
        if subs or len(subs) > 0:
            for sub in subs:
                if sub.submitted_by.user == self.request.user:
                    return True
        return False