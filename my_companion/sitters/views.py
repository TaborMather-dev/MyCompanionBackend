from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Sitter
from .serilizers import SitterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SitterList(APIView):

    def get(self, request):
        sitter = Sitter.objects.all()
        serializer = SitterSerializer(sitter, many=True)
        return  Response(serializer.data)

    def post(self, request):
        serializer = SitterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SitterDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Sitter.objects.get(pk=pk)
        except Sitter.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sitter = self.get_object(pk)
        serializer = SitterSerializer(sitter)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sitter = self.get_object(pk)
        serializer = SitterSerializer(sitter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        sitter = self.get_object(pk)
        sitter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
