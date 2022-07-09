# Generated by Django 4.0.6 on 2022-07-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_salesitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesitem',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Delivered', max_length=100, null=True),
        ),
    ]
