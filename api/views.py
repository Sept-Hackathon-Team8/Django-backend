from rest_framework import generics, permissions
from pets.models import Breed, Journey, Pet, Streak
from units.models import Task, Unit
from .serializers import (
    BreedSerializer,
    JourneySerializer,
    PetSerializer,
    StreakSerializer,
    TaskSerializer,
    UnitSerializer,
)
from .permissions import IsAuthorOrReadOnly


class ListBreed(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DetailBreed(generics.RetrieveAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class ListPet(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Pet.objects.filter(owner=user)

    serializer_class = PetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListStreak(generics.ListCreateAPIView):

    queryset = Streak.objects.all()
    serializer_class = StreakSerializer


class UpdateJourney(generics.RetrieveUpdateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class ListUnits(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class ListTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
