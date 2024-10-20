from django import forms
from django.forms.models import inlineformset_factory
from .models import Task, TimeEntry
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TimeEntryForm(forms.ModelForm):
    """
        Form for creating and updating time entries associated with tasks.

        Attributes:
            model: The Django model `TimeEntry`, representing the time entry entity being created or updated.
            fields: The fields from the `TimeEntry` model that will be included in the form.
            widgets: Custom widgets used for rendering specific fields, such as a date picker for the date field 
                    and a rich text editor for the description field.

        Methods:
            __init__: 
                - Initializes the form and applies specific attributes to each field for consistent styling.
                - Updates each field's widget attributes to include a Bootstrap class for styling.

        Expected Output:
            - Renders a form for inputting details of a time entry, including the date, description, and associated task.
            - Ensures that the form fields are styled with Bootstrap classes for a consistent and responsive design.
            - Provides validation based on the model fields for creating or updating a time entry.
    """
    class Meta:
        model = TimeEntry
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': CKEditorUploadingWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(TimeEntryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control col-lg-6'})  


class TaskForm(forms.ModelForm):
    """
        Form for creating and updating tasks in the system.

        Attributes:
            model: The Django model `Task`, representing the task entity being created or updated.
            fields: The fields from the `Task` model that will be included in the form.
            description: A custom field for the task's description that utilizes a rich text editor for enhanced formatting.

        Methods:
            __init__:
                - Initializes the form and applies specific attributes to each field for consistent styling.
                - Updates each field's widget attributes to include a Bootstrap class for styling.

        Expected Output:
            - Renders a form for inputting task details, including the task name, description, and user association.
            - Ensures that the form fields are styled with Bootstrap classes for a consistent and responsive design.
            - Provides validation based on the model fields for creating or updating a task.
    """
    
    class Meta:
        model = Task
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control col-lg-6 center'})

# Formset inline para TimeEntry
TimeEntryFormSet = inlineformset_factory(
    Task,
    TimeEntry,
    extra=1,
    form=TimeEntryForm,
)

