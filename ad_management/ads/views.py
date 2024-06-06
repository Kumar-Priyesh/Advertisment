from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from ads.models import AdLocation, AdSpend, BusinessCrypto
from .serializers import AdLocationSerializer, AdSpendSerializer, BusinessCryptoSerializer
from django.shortcuts import get_object_or_404

class AdLocationViewSet(viewsets.ModelViewSet):
    queryset = AdLocation.objects.all()
    serializer_class = AdLocationSerializer


class AdSpendViewSet(viewsets.ModelViewSet):
    queryset = AdSpend.objects.all()
    serializer_class = AdSpendSerializer
    basename = 'adspend'

    def get_queryset(self):
        location_name = self.request.query_params.get('location')
        if location_name:
            location = get_object_or_404(AdLocation, name=location_name)
            return AdSpend.objects.filter(location=location)
        else:
            return AdSpend.objects.all()

class BusinessCryptoViewSet(viewsets.ModelViewSet):
    queryset = BusinessCrypto.objects.all()
    serializer_class = BusinessCryptoSerializer
    basename = 'businesscrypto'  # Specify basename

    def get_queryset(self):
        location_name = self.request.query_params.get('location')
        if location_name:
            location = get_object_or_404(AdLocation, name=location_name)
            return BusinessCrypto.objects.filter(location=location)
        else:
            return BusinessCrypto.objects.all()
