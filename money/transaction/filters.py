from django_filters import rest_framework as filters
from .models import Transaction


class TransactionFilterSet(filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            "id": ["exact"],
            "txid": ["exact", "contains"],
            "amount": ["exact", "lte", "gte"],
        }
