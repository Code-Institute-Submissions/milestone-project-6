# Generated by Django 2.0.7 on 2018-07-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersuggestions', '0016_auto_20180711_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionadminpage',
            name='github_branch',
            field=models.URLField(blank=True, null=True),
        ),
    ]