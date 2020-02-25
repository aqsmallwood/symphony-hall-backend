from rest_framework import serializers
from events.models import Venue, Performance


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        exclude = []


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        exclude = []