# Generated by Django 4.2.9 on 2024-01-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_ticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
