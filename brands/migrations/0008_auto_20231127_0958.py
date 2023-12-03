# Generated by Django 3.2.5 on 2023-11-27 08:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0007_auto_20231127_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='available_sizes',
            field=models.ManyToManyField(to='brands.MerchandiseAvailableSizes'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 8, 58, 41, 565941, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='merchandiseavailablesizes',
            name='sizes',
        ),
        migrations.AddField(
            model_name='merchandiseavailablesizes',
            name='sizes',
            field=models.CharField(blank=True, choices=[('', ''), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47')], default='', max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='MerchandiseSize',
        ),
    ]