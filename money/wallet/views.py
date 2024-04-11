from django.db.models import Sum
from rest_framework import viewsets
from .models import Wallet
from .serializers import WalletSerializer
from .filters import WalletFilterSet
from decimal import Decimal
from django.db.models.functions import Coalesce


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filterset_class = WalletFilterSet

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(_balance=Coalesce(Sum("transactions__amount"), Decimal(0)))
        )
