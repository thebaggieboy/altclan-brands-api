# Generated by Django 3.2.5 on 2023-12-05 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0014_auto_20231205_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='available_sizes',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='available_size', to='brands.MerchandiseAvailableSizes'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 6, 17, 41, 938258, tzinfo=utc)),
        ),
    ]