from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AdLocationViewSet, AdSpendViewSet, BusinessCryptoViewSet

router = DefaultRouter()
router.register(r'ad-locations', AdLocationViewSet)
router.register(r'ad-spends', AdSpendViewSet)
router.register(r'business-cryptos', BusinessCryptoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
