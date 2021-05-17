from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Task)
# admin.site.register(TaskSubmission)
# admin.site.register(LearningResource)

class InlineLearningResource(admin.TabularInline):
    model = LearningResource
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    inlines = (InlineLearningResource, )
    list_filter = ('sig', )
    list_display = ('topic', 'sig', 'number', 'posted_on', 'deadline')


class TaskSubmissionAdmin(admin.ModelAdmin):
    list_filter = ('submitted_for__sig', 'grading_status')
    list_display = ('submitted_for', 'submitted_by', 'submitted_on', 'grading_status')
    list_editable = ('grading_status', )
    search_fields = ('submitted_by__name', )
    sortable_by = ('submitted_on', )

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskSubmission, TaskSubmissionAdmin)