# Generated by Django 5.0.4 on 2024-04-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wallet",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("label", models.CharField(max_length=255)),
            ],
        ),
    ]
