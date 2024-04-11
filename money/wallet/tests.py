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


@pytest.mark.django_db
def test_wallet_collect_amount_from_transactions():
    wallet = Wallet.objects.create(label='test')
    Transaction.objects.create(
        wallet=wallet,
        txid='1234567890',
        amount=Decimal('1.987654321987654328')
    )
    Transaction.objects.create(
        wallet=wallet,
        txid='0987654321',
        amount=Decimal('2.123456789123456789')
    )

    assert wallet.amount == Decimal('3.580246791357024679')
