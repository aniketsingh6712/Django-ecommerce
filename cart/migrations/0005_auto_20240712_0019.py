# Generated by Django 3.1.14 on 2024-07-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_delivery_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='payment',
            field=models.CharField(max_length=20),
        ),
    ]
