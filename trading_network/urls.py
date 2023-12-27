from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trading_network.apps import TradingNetworkConfig
from trading_network.views import NetworkViewSet

app_name = TradingNetworkConfig.name

router = DefaultRouter()
router.register(r'trading_network', NetworkViewSet, basename='trading_network')


urlpatterns = [
    path('', include(router.urls)),
]