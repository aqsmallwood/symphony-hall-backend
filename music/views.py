from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from music.models import Work, HeardWork, SeenWork
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


class WorkHeardView(APIView):

    def post(self, request, pk):
        work = get_object_or_404(Work, pk=pk)
        user = request.user
        try:
            HeardWork.objects.create(work=work, user=user)
            return Response({'success': True}, status=201)
        except IntegrityError:
            # The user already marked this work as heard, but no harm done
            return Response({'success': True})


    def delete(self, request, pk):
        work = get_object_or_404(Work, pk=pk)
        user = request.user
        try:
            heard_work = HeardWork.objects.get(work=work, user=user)
            heard_work.delete()
            return Response()
        except HeardWork.DoesNotExist:
            return Response()


class WorkSeenView(APIView):

    def post(self, request, pk):
        work = get_object_or_404(Work, pk=pk)
        user = request.user
        try:
            SeenWork.objects.create(work=work, user=user)
        except IntegrityError:
            # The user already marked this work as seen, but no harm done
            pass
        return Response({'success': True}, status=201)

    def delete(self, request, pk):
        work = get_object_or_404(Work, pk=pk)
        user = request.user
        try:
            seen_work = SeenWork.objects.get(work=work, user=user)
            seen_work.delete()
            return Response()
        except SeenWork.DoesNotExist:
            return Response({'success': True})
