from django.urls import path
from .views import BreedsListView, BreedsDetailView
urlpatterns = [
  path('', BreedsListView.as_view(), name="breed_list"),
  path('<uuid:pk>', BreedsDetailView.as_view(), name="breed_detail")
]