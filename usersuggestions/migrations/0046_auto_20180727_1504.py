# Generated by Django 2.0.7 on 2018-07-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersuggestions', '0045_auto_20180727_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestionadminpage',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'not scheduled'), (1, 'scheduled'), (2, 'in progress'), (3, 'completed')], default=0),
        ),
    ]