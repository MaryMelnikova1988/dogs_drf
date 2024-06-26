from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from dogs.models import Dog
from dogs.paginators import DogPaginator
from dogs.permissions import IsModerator, IsDogOwner
from dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer
from dogs.tasks import send_message_about_like


class SetLikeToDog(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request):
        dog = get_object_or_404 (Dog, pk=request.data.get('dog'))
        user = self.request.user

        if not Dog.objects.filter(likes=user).exists():
            dog.likes.add(user)
            message = f'{user.username} {user.email} поставил лайк {dog.name}'
            send_message_about_like.delay(message, user.email, user.telegram)
        else:
            dog.likes.remove(user)
            message = f'{user.username} {user.email} удалил лайк {dog.name}'
        return Response({'message': message})


class DogDetailView(generics.RetrieveAPIView):
    # serializer_class = DogSerializer
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]


class DogListView(generics.ListAPIView):
    serializer_class = DogListSerializer
    # serializer_class = DogSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = DogPaginator


class DogCreateView(generics.CreateAPIView):
    serializer_class = DogSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # с лайва сохранение хозяина собаки, у нас только права владельца по урокам...
    # но в лайве собака была создана в Viewsetах - и этот метод шел к нему.
    # способ на заметку
    # def perform_create(self, serializer):
    #     new_dog = serializer.save(owner=self.request.user)
    #     new_dog.save()

    # решение с лайва # способ на заметку
    # это решение только на группу модераторов
    # def get_permissions(self):
    #     if self.action in ('create', 'destroy',):
    #         self.permission_classes = [IsAuthenticated, ~IsModerator]
    #     elif self.action in ('update', 'retrieve',):
    #         self.permission_classes = [IsAuthenticated, IsModerator]
    #     return super().get_permissions()
    # это решение уже с хозяевами собак
    # Настроить работу с информацией по собакам для владельцев.
    # Завести группу модераторов и в ней сделать возможным только редактирование и просмотр информации по чужим собакам, но не создание и удаление.
    # def get_permissions(self):
    #     if self.action =='create':
    #         self.permission_classes = [IsAuthenticated, ~IsModerator]
    #     elif self.action in ('update', 'retrieve',):
    #         self.permission_classes = [IsAuthenticated, IsDogOwner | IsModerator]
    #     elif self.action == 'destroy':
    #         self.permission_classes = [IsAuthenticated, IsDogOwner]
    #     return super().get_permissions()


class DogUpdateView(generics.UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]


class DogDeleteView(generics.DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]
