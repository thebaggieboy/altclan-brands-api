# Generated by Django 3.2.5 on 2023-11-27 00:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_auto_20231127_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='available_sizes',
            field=models.ManyToManyField(blank=True, null=True, to='brands.MerchandiseAvailableSizes'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 0, 48, 29, 755506, tzinfo=utc)),
        ),
    ]
