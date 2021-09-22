from django.urls import path
from .views import ListBreed, DetailBreed

urlpatterns = [
    path("breeds/", ListBreed.as_view()),
    path("breeds/<uuid:pk>", DetailBreed.as_view()),
]
