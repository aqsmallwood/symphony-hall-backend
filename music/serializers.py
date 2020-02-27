from rest_framework import serializers

from music.models import Work
from people.serializers import ComposerSerializer


class WorkSerializer(serializers.ModelSerializer):
    composers = ComposerSerializer(many=True, read_only=True)

    class Meta:
        model = Work
        exclude = []
