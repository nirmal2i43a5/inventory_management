# Generated by Django 4.0.6 on 2022-08-17 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_alter_product_quantity_alter_returnproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnproduct',
            name='name',
        ),
    ]