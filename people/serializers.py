from rest_framework import serializers

from people.models import Composer, Performer


class ComposerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Composer
        exclude = []


class PerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        exclude = []
