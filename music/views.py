from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from music.models import Work
from music.serializers import WorkSerializer


class WorkViewSet(viewsets.ViewSet):
    def list(self, request):
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        work = get_object_or_404(Work, pk=pk)
        serializer = WorkSerializer(work)
        return Response(serializer.data)
