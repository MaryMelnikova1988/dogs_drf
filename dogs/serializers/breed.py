from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from dogs.models import Breed, Dog
# from dogs.serializers.dog import DogListSerializer

class DogListSerializer(serializers.ModelSerializer):
    breed = SlugRelatedField(slug_field='name', queryset=Breed.objects.all())
    class Meta:
        model = Dog
        fields = ('name', 'breed')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)

class BreedListSerializer(serializers.ModelSerializer):
    # чтобы добавилось количество собак в данной породе
    dog_count = IntegerField()
    class Meta:
        model = Breed
        fields = ('name','dog_count',)

class BreedDetailSerializer(serializers.ModelSerializer):
    dog_this_breed = SerializerMethodField()

    def get_dog_this_breed(self, breed):
        # return [dog.name for dog in Dog.objects.filter(breed=breed)]
        # делаем возвращение словарем через сериализатор
        return DogListSerializer(Dog.objects.filter(breed=breed), many=True).data
    class Meta:
        model = Breed
        fields = "__all__"