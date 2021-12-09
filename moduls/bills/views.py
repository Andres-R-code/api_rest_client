from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from moduls.bills.models import Bill
from moduls.bills.serializers import GetBillsSerializers


class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = GetBillsSerializers
    permission_classes = (IsAuthenticated, )
