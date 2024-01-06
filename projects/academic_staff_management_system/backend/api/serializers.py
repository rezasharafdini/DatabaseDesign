from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        ]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Education
        fields = "__all__"


class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = "__all__"


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Building
        fields = "__all__"
