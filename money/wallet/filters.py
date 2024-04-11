from django_filters import rest_framework as filters
from .models import Wallet


class WalletFilterSet(filters.FilterSet):
    balance__lte = filters.NumberFilter(
        label="Balance is less or equal", method="balance_filter", lookup_expr="lte"
    )
    balance__gte = filters.NumberFilter(
        label="Balance is greater or equal", method="balance_filter", lookup_expr="gte"
    )
    balance = filters.NumberFilter(
        label="Balance", method="balance_filter", lookup_expr="exact"
    )

    def balance_filter(self, queryset, name, value):
        lookup_expression = self.filters[name].lookup_expr
        return queryset.filter(**{f"_balance__{lookup_expression}": value})

    class Meta:
        model = Wallet
        fields = {
            "id": ["exact"],
            "label": ["exact", "contains"],
        }
