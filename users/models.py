from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    roll_no = models.CharField(max_length=20, unique=True, default='')
    bio = models.TextField(default='Write something about yourself here', blank=True)
    branch = models.CharField(max_length=50, default='CSE')
    year = models.IntegerField(default=1)
    section = models.CharField(max_length=1, default='A')
    college_email_id = models.EmailField(verbose_name='College Email', max_length=254, default='@ipec.org.in')
    contact_number = models.CharField(max_length=10, default='')
    profile_image = models.ImageField(default="/media/images/profile/default.jpg", blank=True, upload_to='images/profile/', height_field=None, width_field=None, max_length=None)
    experience = models.TextField(default='', blank=True)
    projects = models.TextField(default='', blank=True)
    CHOICES = (
        ('CHAIR', 'CHAIR'),
        ('VICE_CHAIR', 'VICE CHAIR'),
        ('PRIME_CORE', 'PRIME CORE'),
        ('CORE', 'CORE'),
        ('HEAD', 'SIG HEAD'),
        ('SUB_HEAD', 'SIG SUBHEAD'),
        ('COORDINATOR', 'COORDINATOR'),
        ('SUB_COORDINATOR', 'SUB COORDINATOR'),
        ('MEMBER', 'SIG MEMBER'),
    )
    member_type = models.CharField(max_length=30, choices=CHOICES, default='MEMBER', blank=True)
    is_acm_team = models.BooleanField(default=False, null=True)
    sigs = models.ManyToManyField("sigs.SpecialInterestGroup", blank=True, related_name="sigs_joined")

    def __str__(self) -> str:
        return f'{self.name}_{self.year}_{self.branch}_{self.section}_{self.roll_no}'

    def get_all_task_points(self):
        points:int = 0
        for submission in self.task_submission.all():
            if submission.grading_status:
                points += submission.points_received
        return points


@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_member(sender, instance, **kwargs):
    instance.member.save()


class ACMTeamMember(models.Model):
    member = models.OneToOneField('Member', verbose_name=("Member"), on_delete=models.DO_NOTHING)
    designation = models.CharField(max_length=50, default='Management')
    joined_on = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.designation}_{self.member.name}'