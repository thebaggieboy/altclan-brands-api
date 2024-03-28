# Generated by Django 3.2.5 on 2024-03-28 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 15, 24, 31, 174183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='FxivTPNzJYbI', max_length=250),
        ),
    ]