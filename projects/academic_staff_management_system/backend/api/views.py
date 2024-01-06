from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from . import serializers
from . import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = models.PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
