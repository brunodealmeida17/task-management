from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class home(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "home/home.html"
