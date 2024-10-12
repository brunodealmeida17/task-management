from django.contrib import admin
from .models import Task, TimeEntry

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')


class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'estimated_time', 'description')
    list_filter = ('date', 'task__user')
    search_fields = ('description', 'task__name')


admin.site.register(Task, TaskAdmin)
admin.site.register(TimeEntry, TimeEntryAdmin)