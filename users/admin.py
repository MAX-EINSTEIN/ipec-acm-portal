from django.contrib import admin
from django.contrib.admin.options import StackedInline, TabularInline
from .models import Member, Role

# Register your models here.
# admin.site.register(Member)
# admin.site.register(Role)

class InlineRole(TabularInline):
    model = Role


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'branch', 'year', 'section')
    list_filter = ('sigs', 'year', 'role__designation')
    search_fields = ('name', 'roll_no')
    sortable_by = ('name', )

    inlines = (InlineRole, )



admin.site.register(Member, MemberAdmin)
