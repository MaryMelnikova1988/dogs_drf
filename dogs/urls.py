from rest_framework.routers import SimpleRouter
from django.urls import path

from dogs.apps import DogsConfig
from dogs.views.breed import BreedViewSet
from dogs.views.dog import DogDeleteView, DogUpdateView, DogDetailView, DogListView, DogCreateView
from dogs.views.donation import DonationCreateView

app_name = DogsConfig.name

router = SimpleRouter()
router.register(r'breed', BreedViewSet, basename='breed')

urlpatterns = [
                  path('create/', DogCreateView.as_view(), name='dog_create'),
                  path('', DogListView.as_view(), name='dog_list'),
                  path('<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
                  path('update/<int:pk>/',DogUpdateView.as_view(), name='dog_update'),
                  path('delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
                  path('donation/create/', DonationCreateView.as_view(), name='donation_create'),

              ] + router.urls