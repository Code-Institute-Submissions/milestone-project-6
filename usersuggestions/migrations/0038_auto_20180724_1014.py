# Generated by Django 2.0.7 on 2018-07-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersuggestions', '0037_suggestionadminpage_date_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavorites',
            name='suggestion',
        ),
        migrations.RemoveField(
            model_name='userfavorites',
            name='user',
        ),
        migrations.AlterField(
            model_name='suggestionadminpage',
            name='suggestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersuggestions.Suggestion'),
        ),
        migrations.DeleteModel(
            name='UserFavorites',
        ),
    ]
