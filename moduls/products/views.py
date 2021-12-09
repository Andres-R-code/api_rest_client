from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated


from moduls.products.models import Product
from moduls.products.serializers import GetProductsSerializers

class ProducViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = GetProductsSerializers
    permission_classes = (IsAuthenticated, )