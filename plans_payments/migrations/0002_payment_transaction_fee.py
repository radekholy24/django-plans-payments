# Generated by Django 2.0.9 on 2018-11-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plans_payments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="transaction_fee",
            field=models.DecimalField(decimal_places=2, default="0.0", max_digits=9),
        ),
    ]
