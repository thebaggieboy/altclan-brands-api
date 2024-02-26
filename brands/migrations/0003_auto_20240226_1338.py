# Generated by Django 3.2.5 on 2024-02-26 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_alter_merchandise_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aesthetics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('aesthetic_name', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 12, 38, 49, 708666, tzinfo=utc)),
        ),
    ]
