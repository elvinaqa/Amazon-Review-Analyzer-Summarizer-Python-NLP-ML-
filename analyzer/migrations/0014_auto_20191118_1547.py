# Generated by Django 2.2.6 on 2019-11-18 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0013_auto_20191118_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_user',
        ),
        migrations.AlterField(
            model_name='product',
            name='analyze_date',
            field=models.DateField(default='1990-10-10', verbose_name=datetime.datetime(2019, 11, 18, 15, 47, 51, 864278)),
        ),
    ]
