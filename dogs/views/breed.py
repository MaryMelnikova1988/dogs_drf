from rest_framework.viewsets import ModelViewSet

from dogs.models import Breed
from dogs.serializers.breed import BreedSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer