from rest_framework import generics
from pets.models import Breed
from .serializers import BreedSerializer


class ListBreed(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DetailBreed(generics.RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
