# Generated by Django 3.2.5 on 2023-11-05 20:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20231103_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 20, 52, 28, 444910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 20, 52, 28, 444910, tzinfo=utc)),
        ),
    ]
