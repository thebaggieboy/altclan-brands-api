# Generated by Django 3.2.5 on 2023-12-22 06:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20231218_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default='f56da5eb99c44f68b569770697e7a3c5', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 6, 36, 55, 935374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='yR6sdEBZavha', max_length=250),
        ),
    ]
