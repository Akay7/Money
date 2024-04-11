import factory.fuzzy
import pytest
import factory
from .models import Transaction


TRANSACTIONS_URL = "/api/v1/transaction/"


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    wallet = factory.SubFactory("wallet.tests.WalletFactory")
    amount = factory.fuzzy.FuzzyDecimal(0.0, 100.0)
    txid = factory.fuzzy.FuzzyText(length=32)


@pytest.mark.django_db
def test_wallet_transaction_str():
    transaction = TransactionFactory(
        txid="1234567890",
    )

    assert str(transaction) == "1234567890"


@pytest.mark.django_db
def test_view_transactions(client):
    TransactionFactory.create_batch(10)

    response = client.get(TRANSACTIONS_URL)

    assert response.status_code == 200
    assert len(response.json()["results"]) == 10


@pytest.mark.django_db
def test_view_transactions_filtered_by_amount(client):
    amounts = list(range(0, 110, 10))
    TransactionFactory.create_batch(len(amounts), amount=factory.Iterator(amounts))

    response = client.get(TRANSACTIONS_URL, {"amount__gte": 30, "amount__lte": 55})

    assert response.status_code == 200
    assert len(response.json()["results"]) == 3
