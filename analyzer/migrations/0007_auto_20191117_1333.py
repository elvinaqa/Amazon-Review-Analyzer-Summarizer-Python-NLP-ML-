# Generated by Django 2.2.6 on 2019-11-17 09:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyzer', '0006_auto_20191117_1256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ViewedProducts',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]