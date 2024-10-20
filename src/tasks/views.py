from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from braces.views import GroupRequiredMixin
from .models import Task, TimeEntry
from .forms import TaskForm, TimeEntryFormSet, TimeEntryFilterForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


class TaskLisView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    """
        View that lists all tasks in the system along with their associated time entries.

        Attributes:
            group_required: The group required to access this view. Only users in the "tasks" group can access the list.
            model: The Django model `Task`, representing the task entities that will be listed.
            template_name: The HTML template used to render the task list.
            context_object_name: The context variable name for the list of tasks in the template.

        Methods:
            get_context_data: 
                - Extends the default context with additional information, including time entries related to each task.
                - Iterates over all tasks to gather relevant data, such as estimated hours, task initiation date, and task status.
                - Returns the modified context that includes a list of tasks and their time entries.

            post:
                - Handles POST requests to update the status of a time entry.
                - Fetches the task ID and the new status from the request.
                - Updates the `status` field of the corresponding `TimeEntry` and saves the changes.
                - Redirects back to the task list view after updating the status.

        Expected Output:
            - Renders a task list where each task is associated with its respective time entries.
            - Provides an option to update the status of a task via a dropdown, and the status update happens immediately upon selection.
            - The task list includes fields such as task ID, name, user, description, created date, estimated hours, start date, and status.
    """
    group_required = u"tasks"
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_with_time = []

        for task in context['tasks']:
            time_entries = TimeEntry.objects.filter(task=task)            
            total_estimated_hours = sum(entry.hours_estimated for entry in time_entries)       
            tasks_with_time.append({
                'id': task.id,
                'name': task.name,
                'user': task.user.username, 
                'description': task.description,                
                'stimed': task.created_at.strftime('%d-%m-%Y'),
                'estimated_hours': ', '.join(entry.estimated_time for entry in time_entries), 
                'init_date': ', '.join(entry.date.strftime('%d-%m-%Y') for entry in time_entries),
                'status': ', '.join(entry.status for entry in time_entries),
                'total_estimated_hours': total_estimated_hours  
            })

        context['tasks_with_time'] = tasks_with_time
        return context
    
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')

        if task_id and new_status:
            try:
                task = TimeEntry.objects.get(task=task_id)
                print(task)
                task.status = new_status
                task.save()
            except TimeEntry.DoesNotExist:
                pass

        return redirect(reverse_lazy('task_list')) 

    
class TaskCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    """
        View for creating a new task in the system along with its associated time entries.

        Attributes:
            group_required: The group required to access this view. Only users in the "tasks" group can create a task.
            model: The Django model `Task`, representing the task entity being created.
            form_class: The form class used to create a new task.
            template_name: The HTML template used to render the task creation form.
            success_url: The URL to redirect to after successfully creating a task.

        Methods:
            get_context_data: 
                - Extends the default context to include a formset for time entries related to the task.
                - If a POST request is made, populates the formset with submitted data; otherwise, initializes an empty formset.
                - Returns the modified context that includes the task form and the time entry formset.

            form_valid:
                - Validates the task form and the time entry formset.
                - If both are valid, saves the task and associates the time entries with it.
                - Redirects to the success URL upon successful creation of the task and its time entries.

        Expected Output:
            - Renders a form for creating a new task, including options to add associated time entries.
            - Displays validation errors if the form or formset is not valid.
            - On successful submission, redirects to the task list view.
    """
    group_required = u"tasks"
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['time_entry_formset'] = TimeEntryFormSet(self.request.POST)
        else:
            data['time_entry_formset'] = TimeEntryFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        time_entry_formset = context['time_entry_formset']
        if form.is_valid() and time_entry_formset.is_valid():
            self.object = form.save()
            time_entries = time_entry_formset.save(commit=False)
            for time_entry in time_entries:
                time_entry.task = self.object
                time_entry.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)
        

class TaskUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
        View for updating an existing task in the system along with its associated time entries.

        Attributes:
            group_required: The group required to access this view. Only users in the "tasks" group can update a task.
            model: The Django model `Task`, representing the task entity being updated.
            form_class: The form class used to update an existing task.
            template_name: The HTML template used to render the task update form.
            success_url: The URL to redirect to after successfully updating the task.

        Methods:
            get_context_data: 
                - Extends the default context to include a formset for time entries related to the task being updated.
                - If a POST request is made, populates the formset with submitted data; otherwise, initializes the formset with the current instance.
                - Returns the modified context that includes the task form and the time entry formset.

            form_valid:
                - Validates the task form and the time entry formset.
                - If both are valid, saves the updated task and its associated time entries.
                - Redirects to the success URL upon successful update of the task and its time entries.

        Expected Output:
            - Renders a form for updating the existing task, including options to modify associated time entries.
            - Displays validation errors if the form or formset is not valid.
            - On successful submission, redirects to the task list view.
    """
    group_required = u"tasks"
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('task_list')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['time_entry_formset'] = TimeEntryFormSet(self.request.POST, instance=self.object)
        else:
            data['time_entry_formset'] = TimeEntryFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        time_entry_formset = context['time_entry_formset']
        if form.is_valid() and time_entry_formset.is_valid():
            self.object = form.save()
            time_entries = time_entry_formset.save(commit=False)
            for time_entry in time_entries:
                time_entry.task = self.object
                time_entry.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class TaskDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    """
        View for deleting an existing task from the system.

        Attributes:
            group_required: The group required to access this view. Only users in the "tasks" group can delete a task.
            model: The Django model `Task`, representing the task entity being deleted.
            template_name: The HTML template used to render the confirmation page for task deletion.
            success_url: The URL to redirect to after successfully deleting the task.
            context_object_name: The context variable name for the task being deleted in the template.

        Methods:
            get_context_data: 
                - Provides context data for rendering the confirmation page, including details of the task being deleted.
                - Returns the context that includes the task object.

            post:
                - Handles POST requests to perform the deletion of the task.
                - Deletes the task instance and redirects to the success URL upon successful deletion.

        Expected Output:
            - Renders a confirmation page asking for user confirmation to delete the selected task.
            - Upon confirmation, deletes the task and redirects to the task list view.
            - Provides feedback in case of successful or failed deletion.
    """
    group_required = u"tasks"
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    context_object_name = 'tasks'





class TimeEntryListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    """
    View that lists all time entries in the system with filtering capabilities.

    Attributes:
        group_required: The group required to access this view. Only users in the "time_entries" group can access the list.
        model: The Django model `TimeEntry`, representing the time entry entities that will be listed.
        template_name: The HTML template used to render the time entry list.
        context_object_name: The context variable name for the list of time entries in the template.

    Methods:
        get_queryset: 
            - Overrides the default queryset to apply filters based on user input from the TimeEntryFilterForm.
            - Filters entries based on various criteria like date, estimated time, description, status, user, and task.

        get_context_data: 
            - Adds the filter form to the context for rendering in the template.
            - Returns the modified context that includes the filter form and the filtered time entries.

    Expected Output:
        - Renders a list of time entries with filtering options for date range, estimated time, description, status, user, and task.
    """
    group_required = u"timeEntry"
    model = TimeEntry
    template_name = "tasks/time_entry_list.html"
    context_object_name = 'entries'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TimeEntryFilterForm(self.request.GET)

        if form.is_valid():
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            
            if date_from:
                queryset = queryset.filter(date__gte=date_from)
            if date_to:
                queryset = queryset.filter(date__lte=date_to)
            estimated_time = form.cleaned_data.get('estimated_time')
            if estimated_time:
                queryset = queryset.filter(estimated_time=estimated_time)
            description = form.cleaned_data.get('description')
            if description:
                queryset = queryset.filter(description__icontains=description)
            status = form.cleaned_data.get('status')
            if status:
                queryset = queryset.filter(status=status)
            user = form.cleaned_data.get('user')
            if user:
                queryset = queryset.filter(task__user=user) 
            task = form.cleaned_data.get('task')
            if task:
                queryset = queryset.filter(task=task)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TimeEntryFilterForm(self.request.GET or None)
        return context

