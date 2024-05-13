from django.shortcuts import render

from rest_framework import generics
from .models import Provider
from .serializers import providerSerializer

class ProviderListCreate(generics.ListCreateAPIView):
    queryset=Provider.objects.all()
    serializer_class=providerSerializer