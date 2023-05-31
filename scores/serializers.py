from rest_framework import serializers
from .models import Peasant


class PeasantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peasant
        fields = ("username", "score", "achievements", )
