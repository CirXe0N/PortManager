from django.db.models import Q
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ShipSerializer
from web.models import Ship


class ShipsView(APIView):
    """
    A view for the users and admins.
    """
    authentication_classes = (authentication.TokenAuthentication,)

    @staticmethod
    def get(request, ship_slug):
        """
        Get Ship Details
        """
        ships = Ship.objects.filter((Q(ship_id=ship_slug) | Q(name=ship_slug)))
        serializer = ShipSerializer(ships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
