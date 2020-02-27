from rest_framework.routers import DefaultRouter

from music.views import WorkViewSet


router = DefaultRouter()
router.register(r'works', WorkViewSet, basename='work')
urlpatterns = router.urls
