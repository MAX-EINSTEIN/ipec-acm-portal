from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    roll_no = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50, default='CSE')
    year = models.IntegerField(default=1)
    section = models.CharField(max_length=1, default='A')
    college_email_id = models.EmailField(verbose_name='College Email', max_length=254, default='@ipec.org.in')
    contact_number = models.CharField(max_length=10, default='')
    profile_image = models.ImageField(null=True, blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    experience = models.TextField(default='', blank=True)
    projects = models.TextField(default='', blank=True)
    member_type = models.CharField(max_length=20, default='SIG MEMBER', blank=True)
    is_acm_team = models.BooleanField(default=False, null=True)
    sigs = models.ManyToManyField("sigs.SpecialInterestGroup", blank=True)
    submissions = models.ManyToManyField("tasks.TaskSubmission", blank=True)

    def __str__(self) -> str:
        return f'{self.name}_{self.year}_{self.branch}_{self.section}_{self.roll_no}'


class ACMTeamMember(models.Model):
    member = models.OneToOneField('Member', verbose_name=("ACM Team Member"), on_delete=models.DO_NOTHING)
    designation = models.CharField(max_length=50, default='Management')
    joined_on = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f'{self.designation}_{self.member.name}'