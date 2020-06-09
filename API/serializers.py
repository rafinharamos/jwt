from rest_framework.serializers import ModelSerializer
from core.models import Sales, Administration


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class AdministrationSerializer(ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'
