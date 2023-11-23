# Generated by Django 3.2.5 on 2023-11-23 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='merchandise_type',
            field=models.CharField(blank=True, choices=[('Tops', 'Tops'), ('Pants', 'Pants'), ('Sweaters', 'Sweaters'), ('T-Shirts', 'T-Shirts'), ('Jackets', 'Jackets'), ('Denim', 'Denim'), ('Watches', 'Watches'), ('Wallets', 'Wallets'), ('Bags', 'Bags'), ('Sunglasses', 'Sunglasses'), ('Hats and Caps', 'Hats and Caps'), ('Belts', 'Belts'), ('Shoes ', 'Shoes'), ('Slides ', 'Slides'), ('Bracelets ', 'Bracelets'), ('Pendants ', 'Pendants'), ('Sweatshirts', 'Sweatshirts'), ('Hoodies', 'Hoodies'), ('Masks', 'Masks'), ('Lumberjacks & Vintage', 'Lumberjacks and Vintage'), ('Piercings & Studs', 'Piercings & Studs'), ('Baggy Wears', 'Baggy Wears'), ('Tattoos', 'Tattoos'), ('Chains & Necklaces', 'Chains & Necklaces'), ('Vintage Shirts', 'Vintage Shirts'), ('Native Wears', 'Native Wears'), ('Watches', 'Watches'), ('Wallets', 'Wallets'), ('Bags', 'Bags'), ('Sunglasses', 'Sunglasses'), ('Hats and Caps', 'Hats and Caps'), ('Belts', 'Belts'), ('Skating', 'Skating'), ('Hoodies', 'Hoodies'), ('Baggy Wears', 'Baggy Wears'), ('Rings', 'Rings'), ('Joggers', 'Joggers'), ('Jeans', 'Jeans')], default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='category',
            field=models.CharField(blank=True, choices=[('Choose your desired collection', 'Choose your desired collection'), ('Tees', 'Tees'), ('Rings', 'Rings'), ('Joggers', 'Joggers'), ('Jeans', 'Jeans')], default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 10, 46, 40, 405135, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandiseavailablesizes',
            name='sizes',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47')], default='', max_length=250, null=True),
        ),
    ]
