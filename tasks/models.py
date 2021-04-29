from django.db import models

# Create your models here.
class Task(models.Model):
    number = models.IntegerField()
    topic = models.CharField(max_length=50)
    description = models.TextField()
    points = models.IntegerField()
    sig = models.OneToOneField("sigs.SpecialInterestGroup", on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    resources = models.ManyToManyField("LearningResource", blank=True)

    def __str__(self) -> str:
        return f'{str(self.sig)}_Task_{self.id}'
    

class LearningResource(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.type}_{self.name}'


class TaskSubmission(models.Model):
    submitted_by = models.ForeignKey("users.Member", on_delete=models.DO_NOTHING)
    submitted_on = models.DateTimeField(auto_now_add=True)
    submitted_for = models.OneToOneField("Task", on_delete=models.DO_NOTHING)
    files = models.URLField(max_length=200)
    points_received = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False) 
