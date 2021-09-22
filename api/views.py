from rest_framework import generics
from pets.models import Breed
from .serializers import BreedSerializer


class BreedAPIView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
