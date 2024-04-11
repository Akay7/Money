from django.db import models


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    wallet = models.ForeignKey(
        "wallet.Wallet", related_name="transactions", on_delete=models.CASCADE
    )
    txid = models.CharField(max_length=32, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)

    def __str__(self):
        return self.txid
