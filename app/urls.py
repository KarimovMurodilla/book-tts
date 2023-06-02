from django.urls import path

from .views import BookCreateView, ResultDetailView

urlpatterns = [
    path('', BookCreateView.as_view(), name='book'),
    path('<int:pk>/', ResultDetailView.as_view(), name='result'),
]