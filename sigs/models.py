from django.db import models
from django.urls import reverse

# Create your models here.
class SpecialInterestGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/sigs/')
    session = models.IntegerField()
    management = models.ManyToManyField("users.Member", blank=True, limit_choices_to={'user__is_staff': True})
    group_link = models.URLField(max_length=200, null=True, blank=True)
    syllabus_link = models.URLField(max_length=200, null=True, blank=True)

    def clean(self) -> None:
        self.name = str(self.name).lower()

    def __str__(self):
        return f'SIG {self.name.upper()} {self.session}'

    def get_absolute_url(self):
        return reverse("sigs:sig", kwargs={"name": self.name})
    
