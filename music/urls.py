from django.urls import path
from rest_framework.routers import DefaultRouter

from music.views import WorkViewSet, WorkHeardView, WorkSeenView


router = DefaultRouter()
router.register(r'works', WorkViewSet, basename='work')

music_urlpatterns = [
    path('works/<int:pk>/heard/', WorkHeardView.as_view(), name='work-heard'),
    path('works/<int:pk>/seen/', WorkSeenView.as_view(), name='work-seen')
]

urlpatterns = router.urls + music_urlpatterns

