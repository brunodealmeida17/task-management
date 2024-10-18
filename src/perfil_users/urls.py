from django.urls import path
from .views import ProfileListView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView, PositionCreateView

urlpatterns = [
    

    path('', ProfileListView.as_view(), name='profile_list'),
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile_delete'),

    path('position-create/', PositionCreateView.as_view(), name='position_create'),
]
