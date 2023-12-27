from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trading_network.apps import TradingNetworkConfig
from trading_network.views import NetworkViewSet

app_name = TradingNetworkConfig.name

router = DefaultRouter()
router.register(r'network', NetworkViewSet, basename='network')


urlpatterns = [
    path('api/', include(router.urls)),
]