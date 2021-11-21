from django.urls import path
from .views import (
    home,
    sorting,
    sorting_result,
    results,
)

urlpatterns = [
    path('', home, name="home"),
    path('sorting', sorting, name="sorting"),
    path('sorting-result/<int:id>', sorting_result, name="sorting-result"),
    path('results', results, name="results"),
]