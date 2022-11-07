
from rest_framework import serializers

from posts.models import Person, Species, Car

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('name', 'birth_year', 'eye_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language')

class CarSerializer(serializers.ModelSerializer):
   class Meta:
       model = Car
       fields = ('name', 'color', 'brand')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'color', 'brand')
