from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from educator.serializers import EducatorSerializer
from educator.models import Educator

# Create your views here.
class ListEducatorAPIView(ListAPIView):
    """This endpoint list all of the available educator from the database"""
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer

class CreateEducatorAPIView(CreateAPIView):
    """This endpoint allows for creation of a educator"""
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer

class UpdateEducatorAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific educator"""
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer

class DeleteEducatorAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific educator"""
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer