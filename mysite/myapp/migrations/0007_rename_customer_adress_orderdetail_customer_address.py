# Generated by Django 4.1.4 on 2025-06-06 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_orderdetail_customer_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='customer_adress',
            new_name='customer_address',
        ),
    ]
