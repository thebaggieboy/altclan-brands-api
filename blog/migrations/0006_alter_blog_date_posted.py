# Generated by Django 3.2.5 on 2024-04-26 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 12, 8, 43, 879600, tzinfo=utc)),
        ),
    ]
