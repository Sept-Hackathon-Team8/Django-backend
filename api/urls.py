from django.urls import path, include
from .views import ListBreed, DetailBreed

urlpatterns = [
    # Third Party
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # Local
    path("breeds/", ListBreed.as_view()),
    path("breeds/<uuid:pk>", DetailBreed.as_view()),
]
