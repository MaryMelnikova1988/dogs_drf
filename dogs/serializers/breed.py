from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from dogs.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)

class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)

class BreedDetailSerializer(serializers.ModelSerializer):
    dog_this_breed = SerializerMethodField()

    def get_dog_this_breed(self, breed):
        return [dog.name for dog in Dog.objects.filter(breed=breed)]
    class Meta:
        model = Breed
        fields = "__all__"