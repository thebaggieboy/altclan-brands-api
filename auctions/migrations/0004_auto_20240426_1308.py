# Generated by Django 3.2.5 on 2024-04-26 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20240426_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 12, 8, 43, 833679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='auctions',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 12, 8, 43, 833679, tzinfo=utc)),
        ),
    ]
