# Generated by Django 2.0.7 on 2018-07-05 15:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0011_auto_20180705_1547'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coins',
            new_name='UserCoins',
        ),
    ]
