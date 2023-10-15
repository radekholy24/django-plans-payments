# Generated by Django 4.1.4 on 2022-12-09 17:37

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plans_payments", "0003_auto_20201006_0855"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="billing_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
