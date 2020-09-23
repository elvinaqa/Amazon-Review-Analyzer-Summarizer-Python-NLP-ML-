# Generated by Django 2.2.6 on 2019-11-18 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0010_product_analyze_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='analyze_date',
            field=models.DateField(default='1990-10-10', verbose_name=datetime.datetime(2019, 11, 18, 15, 42, 8, 529910)),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]
