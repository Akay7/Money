from decimal import Decimal
from transaction.tests import TransactionFactory
from transaction.models import Transaction
from wallet.models import Wallet
import pytest
import factory


WALLET_URL = "/api/v1/wallet/"


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    label = factory.fuzzy.FuzzyText(length=255)


@pytest.mark.django_db
def test_wallet_balance_0():
    wallet = WalletFactory()

    assert wallet.balance == Decimal("0.0")


@pytest.mark.django_db
def test_wallet_collect_balance_from_transactions():
    wallet = WalletFactory()
    TransactionFactory(
        wallet=wallet, txid="1234567890", amount=Decimal("1.987654321987654328")
    )
    TransactionFactory(
        wallet=wallet, txid="0987654321", amount=Decimal("2.123456789123456789")
    )

    assert wallet.balance == Decimal("4.111111111111111117")


@pytest.mark.django_db
def test_view_wallets(client):
    WalletFactory.create_batch(10)

    response = client.get(WALLET_URL)

    assert response.status_code == 200
    assert len(response.json()["results"]) == 10
