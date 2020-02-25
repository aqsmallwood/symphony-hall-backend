from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from people.models import Composer, Performer
from people.serializers import ComposerSerializer, PerformerSerializer


class ComposerViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        composer = get_object_or_404(Composer, pk=pk)
        serializer = ComposerSerializer(composer)
        return Response(serializer.data)

    def list(self, request):
        queryset = Composer.objects.all()
        serializer = ComposerSerializer(queryset, many=True)
        return Response(serializer.data)


class PerformerViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        performer = get_object_or_404(Performer, pk=pk)
        serializer = PerformerSerializer(performer)
        return Response(serializer.data)

    def list(self, request):
        queryset = Performer.objects.all()
        serializer = PerformerSerializer(queryset, many=True)
        return Response(serializer.data)
