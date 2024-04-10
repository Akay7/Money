from decimal import Decimal
from transaction.models import Transaction
from wallet.models import Wallet
import pytest


@pytest.mark.django_db
def test_wallet_transaction_str():
    transaction = Transaction.objects.create(
        wallet=Wallet.objects.create(),
        txid='1234567890',
        amount=Decimal('1.234567890123456789')
    )
    assert str(transaction) == '1234567890'



@pytest.mark.django_db
def test_wallet_amount_0():
    wallet = Wallet.objects.create(label='test')
    assert wallet.amount == Decimal('0.0')
