from rest_framework import generics, permissions, views, response
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
from pets.models import Breed, Journey, Pet, Streak, Assesment
from units.models import Task, Unit
from .serializers import (
    AssesmentListSerializer,
    AssesmentSerializer,
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
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ListAssessments(generics.ListCreateAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer


# TODO: Move assessmentTree logic outside the view
class ListPetAssesments(views.APIView):
    def post(self, request):
        request_body = json.loads(request.body)
        pet_pk = request_body["pet"]
        qs = Assesment.objects.filter(pet__id=pet_pk)
        data = AssesmentListSerializer(qs, many=True, context={"request": request}).data
        if data:
            qs = Unit.objects.all()
            units = UnitSerializer(qs, many=True, context={"request": request}).data
            # print([task["title"] for unit in units for task in unit["tasks"]])
            assessmentTree = [
                [{"ruff": 0, "great": 0} for task in tasks]
                for tasks in [unit["tasks"] for unit in units]
            ]
            for assessment in data:
                assessmentItem = assessmentTree[assessment["unit"] - 1][
                    assessment["task"] - 1
                ]
                if assessment["success"]:
                    assessmentItem["great"] += 1
                else:
                    assessmentItem["ruff"] += 1

            return response.Response(
                {"message": "success", "data": assessmentTree}, status=200
            )
        return response.Response(
            {"message": "no data available", "success": False}, status=404
        )
