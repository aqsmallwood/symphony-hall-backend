from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_jwt.views import obtain_jwt_token


def index_view(request):
    return HttpResponse("Hello world")


API_ROUTE = 'api/v1/'

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path(API_ROUTE + 'token/', obtain_jwt_token),
    path(API_ROUTE, include('users.urls')),
    path(API_ROUTE, include('people.urls')),
    path(API_ROUTE, include('events.urls')),
    path(API_ROUTE, include('music.urls')),
]
