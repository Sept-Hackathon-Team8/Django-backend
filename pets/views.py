from django.shortcuts import render
from django.views.generic import ListView
from .models import Breed

# Create your views here.


class BreedsListView(ListView):
    model = Breed
