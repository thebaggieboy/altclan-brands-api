# Generated by Django 3.2.5 on 2023-12-15 13:32

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20231215_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='available_sizes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 13, 31, 58, 605226, tzinfo=utc)),
        ),
    ]
