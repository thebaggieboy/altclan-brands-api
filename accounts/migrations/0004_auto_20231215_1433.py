# Generated by Django 3.2.5 on 2023-12-15 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20231215_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 13, 33, 52, 192331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 13, 33, 52, 192331, tzinfo=utc)),
        ),
    ]
