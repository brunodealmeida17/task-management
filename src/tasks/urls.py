from django.urls import path
from .views import TaskLisView, TaskCreateView, TaskUpdateView, TaskDeleteView, TimeEntryListView

urlpatterns = [
    path('', TaskLisView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),

     path('time-entries/', TimeEntryListView.as_view(), name='time_entry_list'),
]
