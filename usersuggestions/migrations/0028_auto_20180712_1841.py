# Generated by Django 2.0.7 on 2018-07-12 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersuggestions', '0027_auto_20180712_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestionadminpage',
            old_name='date_time_started',
            new_name='date_started',
        ),
        migrations.RenameField(
            model_name='suggestionadminpage',
            old_name='expected_completion_date_time',
            new_name='expected_completion_date',
        ),
    ]
