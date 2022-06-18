from rest_framework import serializers
from product.models import Event as EventModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["title", "content", "start_propose_date", "end_propose_date"]



