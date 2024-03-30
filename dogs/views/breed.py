from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from dogs.serializers.breed import *


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    # переопределяем каврисет, чтобы добавилось количество собак в данной породе / добавили функцию на лист вместо этого/
    # queryset = Breed.objects.annotate(dog_count=Count("dog"))
    # serializer_class = BreedDetailSerializer
    default_serializer = BreedSerializer
    serializers = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,
    }

    def get_serializer_class(self, *args, **kwargs):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(dog_count=Count("dog"))
        return super().list(request, *args, **kwargs)

