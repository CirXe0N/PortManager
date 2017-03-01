from rest_framework import serializers
from web.models import Ship


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        exclude = ('id', 'captain',)
