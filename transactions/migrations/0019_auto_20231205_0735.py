# Generated by Django 3.2.5 on 2023-12-05 06:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_auto_20231205_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 6, 35, 56, 297485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default='aScRxLGM', max_length=250, null=True),
        ),
    ]