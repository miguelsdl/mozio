from rest_framework import serializers
from api.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone', 'language', 'currency', )


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = ('id', 'provider', 'name', 'price', 'polygon', )
