from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from braces.views import GroupRequiredMixin
from .models import CustomUser, Position
from .forms import CustomUserForm, CustomUserUpdateForm, PositionForm, GroupForm
from django.contrib.auth.models import Group
from django.contrib import messages


class ProfileListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    """
        View that lists all profiles in the system.

        Attributes:
            model: The `CustomUser` model, representing the profiles being listed.
            template_name: The HTML template used to render the list of profiles.
            context_object_name: The context variable name for the profiles list in the template.

        Methods:
            get_context_data:
                - Extends the base context to include additional forms and position data.
                - Adds `CustomUserForm` for creating users and `PositionForm` for assigning positions.
                - Retrieves and provides all available positions to the template.
    """
    group_required = u"users"
    model = CustomUser
    template_name = "perfil_users/profile_list.html"
    context_object_name = "profiles"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user_form'] = CustomUserForm()
        context['position_form'] = PositionForm
        context['positions'] = Position.objects.all()  # Obter todas as posições
        return context


class ProfileCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    """
        View to create a new user profile.

        Attributes:
            model: The `CustomUser` model, representing the user profile being created.
            form_class: The `CustomUserForm`, which is used for profile creation.
            template_name: The HTML template used to render the form.
            success_url: The URL to redirect to upon successful profile creation.
            success_message: A message indicating the successful creation of a user.

        Methods:
            form_valid:
                - Saves the user profile and displays a success message.
                - Redirects to the profile list upon successful submission.
    """
    group_required = u"users"
    model = CustomUser
    form_class = CustomUserForm
    template_name = "perfil_users/profile_form.html"
    success_url = reverse_lazy('profile_list')
    success_message = "Usuário criado com sucesso!"

    def form_valid(self, form):
        # Salvar o usuário
        form.save()

        messages.success(self.request, "Usuário criado com sucesso!")        
        return super().form_valid(form)


class ProfileUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
        View to update an existing user profile.

        Attributes:
            model: The `CustomUser` model, representing the user profile being updated.
            form_class: The `CustomUserUpdateForm`, which is used to handle profile updates.
            template_name: The HTML template used to render the form.
            success_url: The URL to redirect to upon successful profile update.

        Methods:
            form_valid:
                - Handles any additional logic before saving the updated profile.
                - Displays a success message and redirects to the profile list.
    """
    group_required = u"users"
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "perfil_users/profile_form.html"
    success_url = reverse_lazy('profile_list')

    
    def form_valid(self, form):
        # Lógica adicional antes de salvar, se necessário
        
        messages.success(self.request, "Usuário atualizado com sucesso!")       
        return super().form_valid(form)


class ProfileDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    """
        View to delete an existing user profile.

        Attributes:
            model: The `CustomUser` model, representing the user profile being deleted.
            template_name: The HTML template used to confirm the deletion.
            success_url: The URL to redirect to after the profile is successfully deleted.
            context_object_name: Context variable name for the profile being deleted.
    """

    group_required = u"users"
    model = CustomUser
    template_name = "perfil_users/profile_confirm_delete.html"
    success_url = reverse_lazy('profile_list')
    context_object_name = "profiles"


class PositionCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    """
        View to create a new position.

        Attributes:
            model: The `Position` model, representing the position entity.
            form_class: The `PositionForm`, which is used to create new positions.
            template_name: The HTML template used to render the form.
            success_url: The URL to redirect to upon successful position creation.

        Methods:
            form_valid:
                - Saves the new position and redirects to the profile list.
    """
    group_required= u"users"
    model = Position
    form_class = PositionForm
    template_name = 'perfil_users/position_form.html'
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        # Salvar o usuário
        form.save()
        return super().form_valid(form)
    

class GroupListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    """
        View that lists all groups in the system.

        Attributes:
            model: The `Group` model, representing the groups being listed.
            template_name: The HTML template used to render the list of groups.
            context_object_name: Context variable name for the groups list.
    """
    group_required = u"users"
    model = Group
    template_name = 'perfil_users/group_crud.html'
    context_object_name = 'groups'



class GroupCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    """
        View to create a new group.

        Attributes:
            model: The `Group` model, representing the group entity being created.
            form_class: The `GroupForm`, which is used for group creation.
            template_name: The HTML template used to render the form.
            success_url: The URL to redirect to upon successful group creation.

        Methods:
            form_valid:
                - Displays a success message and saves the new group.
                - Redirects to the group list upon successful form submission.
            get_context_data:
                - Adds the list of all existing groups to the context for display.
    """
    group_required = u"users"
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_crud.html'
    success_url = reverse_lazy('group_crud')
    
    def form_valid(self, form):
        messages.success(self.request, "Grupo criado com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()  # Para listar os grupos
        return context



class GroupUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
        View to update an existing group.

        Attributes:
            model: The `Group` model, representing the group entity being updated.
            form_class: The `GroupForm`, which is used to update the group.
            template_name: The HTML template used to render the form.
            success_url: The URL to redirect to upon successful group update.

        Methods:
            form_valid:
                - Displays a success message and saves the updated group.
                - Redirects to the group list after successful submission.
            get_context_data:
                - Adds the list of all existing groups to the context for display.
    """
    group_required = u"users"
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_crud.html'
    success_url = reverse_lazy('group_crud')
    
    def form_valid(self, form):
        messages.success(self.request, "Grupo atualizado com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()  # Para listar os grupos
        return context
    
    
class GroupDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    """
        View to delete an existing group.

        Attributes:
            model: The `Group` model, representing the group entity being deleted.
            template_name: The HTML template used to confirm the deletion.
            success_url: The URL to redirect to after the group is successfully deleted.

        Methods:
            get_context_data:
                - Adds the list of all groups to the context.
                - Sets `form_action` to 'delete' to indicate the action being performed.
    """
    group_required = u"users"
    model = Group
    template_name = 'groups/group_crud.html'
    success_url = reverse_lazy('group_crud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()  # Lista de grupos para exibir
        context['form_action'] = 'delete'  # Ação que está sendo realizada
        return context
   