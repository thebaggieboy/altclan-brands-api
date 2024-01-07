# Generated by Django 3.2.5 on 2024-01-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(blank=True, max_length=250, null=True)),
                ('community_type', models.CharField(blank=True, max_length=250, null=True)),
                ('community_description', models.TextField(default='')),
                ('display_image', models.URLField()),
            ],
        ),
    ]
