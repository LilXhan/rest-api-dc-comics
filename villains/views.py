from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Villain
from .serializers import VillainSerializer

class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all().order_by('name')
    serializer_class = VillainSerializer
    permission_classes = [IsAuthenticated]