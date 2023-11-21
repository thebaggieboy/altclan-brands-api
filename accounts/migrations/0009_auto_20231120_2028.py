# Generated by Django 3.2.5 on 2023-11-20 19:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20231117_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 19, 28, 26, 757499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='branduser',
            name='brand_type',
            field=models.CharField(choices=[('Clothing & Apparel', 'Clothing & Apparel'), ('Accessories', 'Accessories'), ('Arts & Aesthetics', 'Arts & Aesthetics'), ('Footwears & Canvas', 'Footwears & Canvas'), ('Enigmas', 'Enigmas'), ('Watches', 'Watches'), ('Skates', 'Skates'), ('Caps', 'Caps'), ('Masks', 'Masks'), ('Gothic', 'Gothic')], default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 19, 28, 26, 756336, tzinfo=utc)),
        ),
    ]
