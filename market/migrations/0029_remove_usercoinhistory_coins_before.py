# Generated by Django 2.0.7 on 2018-07-16 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0028_usercoinhistory_coins_before'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoinhistory',
            name='coins_before',
        ),
    ]
