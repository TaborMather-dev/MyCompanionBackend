from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Pet
from .serializers import PetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PetList(APIView):

    def get(self, request):
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        return  Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetail(APIView):

    def get_object(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pet = self.get_object(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)