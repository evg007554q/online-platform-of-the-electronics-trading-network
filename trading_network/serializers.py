from rest_framework import serializers
from trading_network.models import Network


class NetworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'
        # запретить обновление через API
        read_only_fields = ['debt_to_supplier']