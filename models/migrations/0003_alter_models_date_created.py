# Generated by Django 3.2.5 on 2024-03-28 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_models_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 15, 24, 31, 174183, tzinfo=utc)),
        ),
    ]
