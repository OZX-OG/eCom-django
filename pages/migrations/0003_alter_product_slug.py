# Generated by Django 4.2.9 on 2024-01-15 11:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_product_photo_product_produc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True),
        ),
    ]
