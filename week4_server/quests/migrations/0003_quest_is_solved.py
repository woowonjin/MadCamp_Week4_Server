# Generated by Django 3.1.5 on 2021-01-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0002_quest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='is_solved',
            field=models.BooleanField(default=False),
        ),
    ]
