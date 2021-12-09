from rest_framework.serializers import ModelSerializer
from moduls.products.models import Product

class GetProductsSerializers(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'