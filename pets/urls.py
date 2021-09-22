from django.urls import path
from .views import BreedsListView
urlpatterns = [
  path('', BreedsListView.as_view(), name="breed_list")
]