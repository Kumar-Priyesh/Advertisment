from rest_framework import serializers
from .models import AdLocation, AdSpend, BusinessCrypto

class AdLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdLocation
        fields = '__all__'

class AdSpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdSpend
        fields = '__all__'

class BusinessCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCrypto
        fields = '__all__'
