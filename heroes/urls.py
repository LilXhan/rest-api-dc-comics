from rest_framework import routers
from .views import HeroViewSet

router = routers.DefaultRouter()

router.register(r'heroes', HeroViewSet, basename='heroes')

urlpatterns = router.urls
