from django_filters import rest_framework as filters
from .models import Wallet


class WalletFilterSet(filters.FilterSet):
    class Meta:
        model = Wallet
        fields = {
            "id": ["exact"],
            "label": ["exact", "contains"],
            "balance": ["exact", "lte", "gte"],
        }
