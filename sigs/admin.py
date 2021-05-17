from django.contrib import admin
from .models import SpecialInterestGroup

# Register your models here.
# admin.site.register(SpecialInterestGroup)

class SpecialInterestGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('management', )

admin.site.register(SpecialInterestGroup, SpecialInterestGroupAdmin)