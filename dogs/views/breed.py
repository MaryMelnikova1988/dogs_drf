from rest_framework.viewsets import ModelViewSet

from dogs.serializers.breed import *


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    # serializer_class = BreedDetailSerializer
    default_serializer = BreedSerializer
    serializers = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,
    }

    def get_serializer_class(self, *args, **kwargs):
        return self.serializers.get(self.action, self.default_serializer)
