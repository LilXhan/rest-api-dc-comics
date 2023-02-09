from rest_framework import serializers
from .models import Villain

class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villain
        fields = ('name', 'alias')