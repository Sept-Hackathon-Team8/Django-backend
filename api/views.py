from rest_framework import generics
from pets.models import Breed
from .serializers import BreedSerializer
from .permissions import IsAuthorOrReadOnly


class ListBreed(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DetailBreed(generics.RetrieveAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
