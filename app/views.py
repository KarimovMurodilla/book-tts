from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'app/service.html'
    fields = ('book',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ResultDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'app/result.html'