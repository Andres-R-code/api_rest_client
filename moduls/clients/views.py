from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from moduls.clients.models import Client
from moduls.clients.serializers import GetClientsSerializers


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = GetClientsSerializers
    permission_classes = (IsAuthenticated, )
