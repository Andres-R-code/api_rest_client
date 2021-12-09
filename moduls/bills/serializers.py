from django.db.models import fields
from rest_framework.serializers import ModelSerializer


from moduls.bills.models import Bill
from moduls.clients.models import Client
from moduls.clients.serializers import GetClientsSerializers

class AuxClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'first_name','last_name', 'document')

class GetBillsSerializers(ModelSerializer):
    client = AuxClientSerializer(read_only=True, many=True)

    class Meta:
        model = Bill
        fields = ('__all__')