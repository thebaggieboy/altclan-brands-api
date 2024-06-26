# Generated by Django 3.2.5 on 2024-04-26 12:25

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aesthetics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('aesthetic_name', models.CharField(blank=True, max_length=250, null=True)),
                ('aesthetic_image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram_username', models.CharField(blank=True, max_length=250, null=True)),
                ('website_link', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('merchandise_name', models.CharField(default='', max_length=250)),
                ('merchandise_color', models.CharField(default='', max_length=250)),
                ('size_type', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('merchandise_type', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('merchandise_description', models.TextField(default='')),
                ('merchandise_details', models.TextField(default='')),
                ('merchandise_gender', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('display_image', models.URLField()),
                ('image_1', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_2', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_3', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_4', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_5', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('labels', models.CharField(choices=[('None', 'None'), ('New Merchandise', 'New Merchandise'), ('Limited Stock', 'Limited Stock'), ('FREE DELIVERY', 'FREE DELIVERY')], default='', max_length=250)),
                ('price', models.IntegerField(null=True)),
                ('delivery_cost', models.FloatField(default=0.0, null=True)),
                ('discount', models.FloatField(default=0.0, null=True)),
                ('slug', models.SlugField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2024, 4, 26, 12, 25, 46, 226723, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='MerchandiseAvailableSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizes', models.CharField(blank=True, choices=[('', ''), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47')], default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchandise_name', models.CharField(default='', max_length=250)),
                ('merchandise_color', models.CharField(default='', max_length=250)),
                ('size_type', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('available_sizes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None)),
                ('available_colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None)),
                ('merchandise_type', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('merchandise_description', models.TextField(default='')),
                ('merchandise_details', models.TextField(default='')),
                ('merchandise_gender', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('display_image', models.URLField()),
                ('image_1', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_2', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_3', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_4', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_5', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('labels', models.CharField(choices=[('None', 'None'), ('New Merchandise', 'New Merchandise'), ('Limited Stock', 'Limited Stock'), ('FREE DELIVERY', 'FREE DELIVERY')], default='', max_length=250)),
                ('price', models.IntegerField(null=True)),
                ('delivery_cost', models.FloatField(default=0.0, null=True)),
                ('discount', models.FloatField(default=0.0, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.billingaddress')),
                ('merchandises', models.ManyToManyField(to='brands.Merchandise')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BrandDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.CharField(blank=True, max_length=250, null=True)),
                ('total_users', models.CharField(blank=True, max_length=250, null=True)),
                ('total_products', models.CharField(blank=True, max_length=250, null=True)),
                ('total_profit', models.CharField(blank=True, max_length=250, null=True)),
                ('total_revenue', models.CharField(blank=True, max_length=250, null=True)),
                ('total_sales', models.CharField(blank=True, max_length=250, null=True)),
                ('total_orders', models.CharField(blank=True, max_length=250, null=True)),
                ('items', models.ManyToManyField(to='brands.Merchandise')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_dashboard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
