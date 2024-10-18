from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from braces.views import GroupRequiredMixin
from .models import CustomUser, Position
from .forms import CustomUserForm, PositionForms



class ProfileListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    """
    View that lists all profiles in the system.

    Attributes:
        queryset: The queryset of all profile instances.
        template_name: The HTML template used to render the list.
        context_object_name: Context variable name for the profiles list.
    """
    group_required = u"users"
    model = CustomUser
    template_name = "perfil_users/profile_list.html"
    context_object_name = "profiles"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user_form'] = CustomUserForm()
        context['position_form'] = PositionForms()
        context['positions'] = Position.objects.all()  # Obter todas as posições
        return context


class ProfileCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    """
    View to create a new profile.

    Attributes:
        model: The Profile model.
        form_class: The ProfileForm used to create the profile.
        template_name: The HTML template for the profile creation.
    """
    group_required = u"users"
    model = CustomUser
    form_class = CustomUserForm
    template_name = "perfil_users/profile_form.html"
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        # Salvar o usuário
        form.save()
        return super().form_valid(form)


class ProfileUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
    View to update an existing profile.

    Attributes:
        model: The Profile model.
        form_class: The ProfileForm used to update the profile.
        template_name: The HTML template for the profile update.
    """
    group_required = u"users"
    model = CustomUser
    form_class = CustomUserForm
    template_name = "perfil_users/profile_form.html"
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar
        return super().form_valid(form)


class ProfileDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    """
    View to delete an existing profile.

    Attributes:
        model: The Profile model.
        template_name: The HTML template for the profile deletion confirmation.
    """
    group_required = u"users"
    model = CustomUser
    template_name = "perfil_users/profile_confirm_delete.html"
    success_url = reverse_lazy('profile_list')

   