# Generated by Django 3.2.5 on 2024-04-08 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 14, 29, 46, 964105, tzinfo=utc)),
        ),
    ]
