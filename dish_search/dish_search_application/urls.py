from django.urls import path
from dish_search_application.views import search

urlpatterns = [
    path('search/', search, name='search'),
]
