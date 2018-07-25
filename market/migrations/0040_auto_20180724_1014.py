# Generated by Django 2.0.7 on 2018-07-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0039_auto_20180718_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoinhistory',
            name='transaction',
            field=models.PositiveSmallIntegerField(choices=[(1, 'submission'), (2, 'upvote'), (3, 'referral'), (4, 'store purchase'), (5, 'initial signup'), (6, 'received referral'), (7, 'suggestion upvoted'), (8, 'suggestion successful'), (9, 'feature suggestion promoted')], default=2),
            preserve_default=False,
        ),
    ]