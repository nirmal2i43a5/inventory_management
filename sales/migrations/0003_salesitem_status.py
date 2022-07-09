# Generated by Django 4.0.6 on 2022-07-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_customer_sold_date_customer_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'out for delivery')], default='Delivered', max_length=100, null=True),
        ),
    ]