from django.urls import path
from .views import BreedAPIView

urlpatterns = [
    path("breeds/", BreedAPIView.as_view()),
]
