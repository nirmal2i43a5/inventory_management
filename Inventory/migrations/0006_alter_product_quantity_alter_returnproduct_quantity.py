# Generated by Django 4.0.6 on 2022-08-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_returnproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Quantity',
            field=models.IntegerField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='returnproduct',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
