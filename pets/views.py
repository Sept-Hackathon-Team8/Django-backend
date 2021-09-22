from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Breed

# Create your views here.


class BreedsListView(ListView):
    model = Breed

class BreedsDetailView(DetailView):
    model = Breed
