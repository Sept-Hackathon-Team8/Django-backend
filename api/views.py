from rest_framework import generics
from pets.models import Breed, Journey, Pet, Streak
from .serializers import BreedSerializer, JourneySerializer, PetSerializer, StreakSerializer
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