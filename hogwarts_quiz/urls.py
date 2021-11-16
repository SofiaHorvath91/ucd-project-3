from django.urls import path
from .views import (
    home,
    sorting,
    sorting_result,
    results,
    feedback,
)

urlpatterns = [
    path('', home, name="home"),
    path('sorting', sorting, name="sorting"),
    path('sorting-result/<int:id>', sorting_result, name="sorting-result"),
    path('results', results, name="results"),
    path('feedback', feedback, name="feedback"),
]