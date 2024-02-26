# Generated by Django 3.2.5 on 2024-02-26 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20240226_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 12, 46, 23, 494298, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='N4AaaT9YQ37n', max_length=250),
        ),
    ]
