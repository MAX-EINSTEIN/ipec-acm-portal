from django.forms import ModelForm
from .models import TaskSubmission

class TaskSubmissionForm(ModelForm):
    
    class Meta:
        model = TaskSubmission
        fields = ('code_files', 'output_files')