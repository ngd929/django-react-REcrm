from django.shortcuts import render
from rest_framework import generics

from .models import Property, PropertyInfo, Geolocation, Customer
from .serializers import PropertySerializer, PropertyInfoSerializer, GeolocationSerializer, CustomerSerializer


class PropertyAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyInfoAPIView(generics.ListCreateAPIView):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer

class GeolocationAPIView(generics.ListCreateAPIView):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer

class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer