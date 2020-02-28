from rest_framework import serializers

from music.models import Work, HeardWork, SeenWork
from people.serializers import ComposerSerializer


class WorkSerializer(serializers.ModelSerializer):
    composers = ComposerSerializer(many=True, read_only=True)

    class Meta:
        model = Work
        exclude = []


class HeardWorkSerializer(serializers.ModelSerializer):
    work = WorkSerializer()

    class Meta:
        model = HeardWork
        fields = ['work']


class SeenWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeenWork
        fields = ['work']