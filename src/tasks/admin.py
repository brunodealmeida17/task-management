from django.contrib import admin
from .models import Task, TimeEntry


class TimeEntryInline(admin.TabularInline):
    """
        Inline for managing time entries within the task form in the admin panel.

        Attributes:
            model: The Django model `TimeEntry`, representing the time entry entity that will be managed inline.
            extra: The number of empty time entries to display in the form for adding new entries.

        Expected Output:
            - Allows for the addition and editing of time entries associated with a task directly within the task form interface.
            - Facilitates the management of time entries without the need to navigate to a separate page.
    """
    model = TimeEntry
    extra = 1  


class TaskAdmin(admin.ModelAdmin):
    """
        Admin configuration for the `Task` model.

        Attributes:
            list_display: Fields to be displayed in the task list, including the task name, responsible user, and creation date.
            search_fields: Fields that can be searched, allowing searches by task name and associated username.
            inlines: List of inline classes to be displayed on the task admin page. In this case, it includes `TimeEntryInline`.

        Expected Output:
            - Renders the admin panel interface for tasks, allowing easy viewing and searching.
            - Allows for the addition and editing of time entries directly on the task page, improving efficiency in task management.
    """

    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    inlines = [TimeEntryInline]


class TimeEntryAdmin(admin.ModelAdmin):
    """
        Admin configuration for the `Task` model.

        Attributes:
            list_display: Fields to be displayed in the task list, including the task name, responsible user, and creation date.
            search_fields: Fields that can be searched, allowing searches by task name and associated username.
            inlines: List of inline classes to be displayed on the task admin page. In this case, it includes `TimeEntryInline`.

        Expected Output:
            - Renders the admin panel interface for tasks, allowing easy viewing and searching.
            - Allows for the addition and editing of time entries directly on the task page, improving efficiency in task management.
    """

    list_display = ('task', 'date', 'estimated_time', 'description')
    list_filter = ('date', 'task__user')
    search_fields = ('description', 'task__name')


admin.site.register(Task, TaskAdmin)
admin.site.register(TimeEntry, TimeEntryAdmin)