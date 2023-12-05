# Generated by Django 3.2.5 on 2023-12-05 07:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0023_auto_20231205_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default='ef8bf62db57e43f991fe63b0368d23c1', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 7, 14, 20, 204252, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='1eSw8fnYRpze', max_length=250),
        ),
    ]
