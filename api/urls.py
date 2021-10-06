from django.urls import path, include
from .views import (
    ListBreed,
    DetailBreed,
    ListPet,
    ListTasks,
    UpdateJourney,
    ListUnits,
    ListPetAssesments,
    ListAssessments,
)

urlpatterns = [
    # Third Party
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # Local
    path("breeds/", ListBreed.as_view()),
    path("breeds/<uuid:pk>", DetailBreed.as_view()),
    path("pets/", ListPet.as_view()),
    path("journey/<uuid:pk>", UpdateJourney.as_view()),
    path("units/", ListUnits.as_view()),
    path("units/tasks/", ListTasks.as_view()),
    path("assessments/", ListAssessments.as_view()),
    path("pet/assessments/", ListPetAssesments.as_view()),
]
