from django.contrib import admin
from django.contrib.admin.options import StackedInline
from .models import Member, ACMTeamMember

# Register your models here.
# admin.site.register(Member)
admin.site.register(ACMTeamMember)

# class InlineACMTeamMember(StackedInline):
#     model = ACMTeamMember

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'branch', 'year', 'section')
    list_filter = ('sigs', 'year', 'member_type')
    search_fields = ('name', 'roll_no')
    sortable_by = ('name', )

    # inlines = (InlineACMTeamMember, )



admin.site.register(Member, MemberAdmin)
