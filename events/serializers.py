from rest_framework import serializers
from events.models import Venue, Performance
from music.serializers import WorkSerializer
from people.serializers import PerformerSerializer


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        exclude = []


class PerformanceSerializer(serializers.ModelSerializer):
    work = WorkSerializer()
    performers = PerformerSerializer(many=True)

    class Meta:
        model = Performance
        exclude = []
