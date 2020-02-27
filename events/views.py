from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from events.models import Venue, Performance
from events.serializers import VenueSerializer, PerformanceSerializer


class VenueViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        venue = get_object_or_404(Venue, pk=pk)
        serializer = VenueSerializer(venue)
        return Response(serializer.data)

    def list(self, request):
        queryset = Venue.objects.all()
        serializer = VenueSerializer(queryset, many=True)
        return Response(serializer.data)


class PerformanceViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        performance = get_object_or_404(Performance, pk=pk)
        serializer = PerformanceSerializer(performance)
        return Response(serializer.data)

    def list(self, request):
        queryset = Performance.objects.all()
        serializer = PerformanceSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
