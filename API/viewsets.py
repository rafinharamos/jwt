from rest_framework.viewsets import ModelViewSet
from core.models import Sales, Administration
from .serializers import SaleSerializer, AdministrationSerializer


class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer


class AdministrationViewSet(ModelViewSet):
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer

# lista de verbos http permitidos por padrão
# http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
