from rest_framework import routers
from .views import VillainViewSet

router = routers.DefaultRouter()

router.register(r'villains', VillainViewSet, basename='villains')

urlpatterns = router.urls