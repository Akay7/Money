from rest_framework import viewsets
from .models import Wallet
from .serializers import WalletSerializer
from .filters import WalletFilterSet


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
