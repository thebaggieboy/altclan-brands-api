# Generated by Django 3.2.5 on 2024-04-01 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20240401_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 22, 15, 39, 771904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='auctions',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 22, 15, 39, 771904, tzinfo=utc)),
        ),
    ]
