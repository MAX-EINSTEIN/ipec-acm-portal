from django.db import models

# Create your models here.
class Task(models.Model):
    number = models.IntegerField()
    topic = models.CharField(max_length=50)
    description = models.TextField()
    points = models.IntegerField()
    sig = models.ForeignKey("sigs.SpecialInterestGroup", on_delete=models.CASCADE, related_name='tasks')
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    # resources = models.ManyToManyField("tasks.LearningResource", blank=True)
    starter_files = models.FileField(upload_to="documents/starter_files/", verbose_name="Starter Files", blank=True, null=True)

    def __str__(self) -> str:
        return f'{str(self.sig)}_Task_{self.number}'

    

class LearningResource(models.Model):
    CONTENT_TYPE = (
        ('Article', 'ARTICLE'),
        ('Video', 'VIDEO'),
        ('Blog', 'BLOG'),
        ('Tool', 'TOOL'),
        ('Demo', 'DEMO'),
    )

    task = models.ForeignKey("tasks.Task", verbose_name=("Learning Resource"), on_delete=models.CASCADE, related_name="resources")
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=CONTENT_TYPE)
    url = models.URLField(max_length=200)


    def __str__(self) -> str:
        return f'{self.type}_{self.name}'


class TaskSubmission(models.Model):
    submitted_by = models.ForeignKey("users.Member", null=True, on_delete=models.DO_NOTHING, blank=True, related_name='task_submission')
    submitted_on = models.DateTimeField(auto_now_add=True)
    submitted_for = models.ForeignKey("Task", null=True, on_delete=models.DO_NOTHING, blank=True, related_name='task_submission')
    code_files = models.FileField(upload_to='submissions/', verbose_name='Code', blank=True, null=True)
    output_files = models.FileField(upload_to='submissions/', verbose_name='Output', blank=True, null=True)
    points_received = models.IntegerField(default=0, null=True, blank=True)
    grading_status = models.BooleanField(default=False, choices=((True, 'GRADED'), (False, 'PENDING')))

    def __str__(self) -> str:
        return f'SIG {self.submitted_for.sig}_TASK#{self.submitted_for.number}_SUBMITTED_BY_{self.submitted_by}'