from django.db import models

# Create your models here.
class SpecialInterestGroup(models.Model):
    name = models.CharField(max_length=50)
    session = models.IntegerField()
    management = models.ManyToManyField("users.ACMTeamMember")
    members = models.ManyToManyField("users.Member", blank=True)
    group_link = models.URLField(max_length=200, null=True, blank=True)
    syllabus_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}_{self.session}'