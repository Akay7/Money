# Generated by Django 5.0.4 on 2024-04-10 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("txid", models.CharField(max_length=32)),
                ("amount", models.DecimalField(decimal_places=18, max_digits=36)),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="wallet.wallet",
                    ),
                ),
            ],
        ),
    ]