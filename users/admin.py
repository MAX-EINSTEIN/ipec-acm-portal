from django.contrib import admin
from .models import Member, ACMTeamMember

# Register your models here.
admin.site.register(Member)
admin.site.register(ACMTeamMember)