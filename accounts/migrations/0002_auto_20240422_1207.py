# Generated by Django 3.2.5 on 2024-04-22 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 22, 11, 7, 35, 651566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='branduser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 22, 11, 7, 35, 645251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 22, 11, 7, 35, 647837, tzinfo=utc)),
        ),
    ]
