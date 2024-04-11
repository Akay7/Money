from django.db import models
from decimal import Decimal


class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

    @property
    def balance(self) -> Decimal:
        if hasattr(self, "_balance"):
            return self._balance
        return sum([t.amount for t in self.transactions.all()] or [Decimal("0.0")])
