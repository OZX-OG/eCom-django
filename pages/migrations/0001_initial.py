# Generated by Django 4.2.9 on 2024-01-15 10:35

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('price', models.FloatField()),
                ('anchor_price', models.FloatField()),
                ('photo', models.ImageField(upload_to='product', verbose_name='Main image')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.categories')),
            ],
        ),
    ]
