from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from trading_network.models import Network
from trading_network.serializers import NetworkSerializers


class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializers
    queryset = Network.objects.all()

    filter_backends = [OrderingFilter]
    filterset_fields = ('country', )































































