# Generated by Django 3.2.5 on 2024-03-28 15:23

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
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 15, 23, 42, 223681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='branduser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 15, 23, 42, 222327, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 15, 23, 42, 223327, tzinfo=utc)),
        ),
    ]
