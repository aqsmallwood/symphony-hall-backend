from django.urls import path
from rest_framework.routers import DefaultRouter

from events.views import VenueViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet, basename='venue')
router.register(r'performances', PerformanceViewSet, basename='performance')
urlpatterns = router.urls
