from rest_framework.serializers import ModelSerializer

from moduls.bills.models import Bill

class GetBillsSerializers(ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'