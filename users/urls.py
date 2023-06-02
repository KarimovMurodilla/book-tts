from django.urls import path, include 

from .views import HomeListView, SignUpView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls'), name='home')
]