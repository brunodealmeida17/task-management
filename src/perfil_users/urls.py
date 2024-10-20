from django.urls import path
from .views import ProfileListView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView, PositionCreateView, GroupListView, GroupCreateView, GroupUpdateView, GroupDeleteView

urlpatterns = [
    

    path('', ProfileListView.as_view(), name='profile_list'),
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile_delete'),

    path('position-create/', PositionCreateView.as_view(), name='position_create'),

    path('group-list/', GroupListView.as_view(), name='group_crud'),
    path('group-create/', GroupCreateView.as_view(), name='group_create'),
    path('group-update/<int:pk>/', GroupUpdateView.as_view(), name='group_update'),
    path('group-delete/<int:pk>/', GroupDeleteView.as_view(), name='group_delete'),
]
