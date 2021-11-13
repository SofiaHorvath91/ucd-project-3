from django.urls import path
from .views import (
    home,
    sorting,
    results,
    feedback,
)

urlpatterns = [
    path('', home, name="home"),
    path('sorting', sorting, name="sorting"),
    path('results', results, name="results"),
    path('feedback', feedback, name="feedback"),
]