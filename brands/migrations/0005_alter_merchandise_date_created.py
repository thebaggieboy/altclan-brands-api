# Generated by Django 3.2.5 on 2023-11-17 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_auto_20231107_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 17, 47, 54, 911561, tzinfo=utc)),
        ),
    ]