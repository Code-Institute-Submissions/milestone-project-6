# Generated by Django 2.0.7 on 2018-07-13 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersuggestions', '0030_auto_20180713_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestionadminpage',
            old_name='is_current_winner',
            new_name='current_winner',
        ),
    ]
