from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from music.models import Work, HeardWork, SeenWork
from music.serializers import WorkSerializer, HeardWorkSerializer, SeenWorkSerializer


class WorkViewSet(viewsets.ViewSet):
    def list(self, request):
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        work = get_object_or_404(Work, pk=pk)
        serializer = WorkSerializer(work)
        return Response(serializer.data)

    def heard(self, request):
        works = HeardWork.objects.filter(user=request.user).values_list(['id'])
        return Response({'works': works})

    def seen(self, request):
        works = SeenWork.objects.filter(user=request.user).values_list(['id'])
        return Response({'works': works})


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


class TrackedWorkView(APIView):
    model = None
    serializer = None

    def get(self, request):
        tracked_works = self.model.objects.filter(
            user=request.user).values_list('work')
        works = Work.objects.filter(id__in=tracked_works)
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)


class WorksHeardView(TrackedWorkView):
    model = HeardWork


class WorksSeenView(TrackedWorkView):
    model = SeenWork
