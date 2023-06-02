from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from .forms import CustomUserCreationForm

from .models import CustomUser


class HomeListView(ListView):
    model = CustomUser
    template_name = 'base.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
