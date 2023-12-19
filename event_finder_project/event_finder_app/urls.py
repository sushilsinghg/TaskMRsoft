# event_finder_app/urls.py
from django.urls import path
from .views import event_search

urlpatterns = [
    path('search/', event_search, name='event_search'),
]
