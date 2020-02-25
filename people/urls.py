from rest_framework.routers import DefaultRouter

from people.views import ComposerViewSet, PerformerViewSet


router = DefaultRouter()
router.register(r'composers', ComposerViewSet, basename='composer')
router.register(r'performers', PerformerViewSet, basename='performer')
urlpatterns = router.urls
