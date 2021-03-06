# Generated by Django 2.1.5 on 2019-01-13 16:54

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=200, populate_from='transliterate_slug', unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='NOT CONFIRMED', max_length=20, verbose_name='Status/Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=200, populate_from='transliterate_slug', unique=True),
        ),
    ]
