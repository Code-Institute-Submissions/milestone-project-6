# Generated by Django 2.0.7 on 2018-07-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_order_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='delivery_required',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
