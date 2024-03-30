from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from dogs.models import Dog
from dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer




class DogDetailView(generics.RetrieveAPIView):
    # serializer_class = DogSerializer
    serializer_class =DogDetailSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]

class DogListView(generics.ListAPIView):
    serializer_class = DogListSerializer
    # serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]

class DogCreateView(generics.CreateAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]

class DogUpdateView(generics.UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]

class DogDeleteView(generics.DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]