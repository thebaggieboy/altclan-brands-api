# Generated by Django 3.2.5 on 2024-03-20 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20240308_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 15, 20, 3, 835669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='branduser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 15, 20, 3, 829207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 15, 20, 3, 833846, tzinfo=utc)),
        ),
    ]
