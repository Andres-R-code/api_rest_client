from rest_framework.serializers import ModelSerializer

from moduls.clients.models import Client


class GetClientsSerializers(ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'first_name','last_name', 'document')

