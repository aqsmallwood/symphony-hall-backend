from django.urls import path
from rest_framework.routers import DefaultRouter

from music.views import WorkViewSet, WorkHeardView, WorkSeenView, WorksHeardView, WorksSeenView


router = DefaultRouter()
router.register(r'works', WorkViewSet, basename='work')

music_urlpatterns = [
    path('works/heard/', WorksHeardView.as_view(), name='works-heard'),
    path('works/seen/', WorksSeenView.as_view(), name='works-seen'),
    path('works/<int:pk>/heard/', WorkHeardView.as_view(), name='work-heard'),
    path('works/<int:pk>/seen/', WorkSeenView.as_view(), name='work-seen')
]

urlpatterns = music_urlpatterns + router.urls
