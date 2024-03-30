from rest_framework import generics

from dogs.models import Dog
from dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer


class DogDetailView(generics.RetrieveAPIView):
    # serializer_class = DogSerializer
    serializer_class =DogDetailSerializer
    queryset = Dog.objects.all()

class DogListView(generics.ListAPIView):
    serializer_class = DogListSerializer
    # serializer_class = DogSerializer
    queryset = Dog.objects.all()
class DogCreateView(generics.CreateAPIView):
    serializer_class = DogSerializer

class DogUpdateView(generics.UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

class DogDeleteView(generics.DestroyAPIView):
    queryset = Dog.objects.all()