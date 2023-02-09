from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Hero
from .serializers import HeroSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticated]