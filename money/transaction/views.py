from rest_framework import viewsets
from .serializers import TransactionSerializer
from .models import Transaction
from .filters import TransactionFilterSet


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilterSet
    ordering_fields = ["id", "txid", "amount"]
