# Generated by Django 2.0.7 on 2018-07-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20180705_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='coins_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
