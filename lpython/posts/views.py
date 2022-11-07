from django.shortcuts import render
from django.http import HttpResponse
from posts.serializers import PersonSerializer, SpeciesSerializer, CarSerializer
from posts.models import Person, Species, Car
from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is the polls app")
    return response

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer

class ListCreateCarView(ListCreateAPIView):
    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    model = Car
    serializer_class = CarSerializer

    def put(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = CarSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Car successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)
