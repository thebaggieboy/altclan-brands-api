# Generated by Django 3.2.5 on 2023-11-27 09:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0008_auto_20231127_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 9, 1, 53, 702514, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandiseavailablesizes',
            name='merchandise_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='size', to='brands.merchandise'),
        ),
    ]
