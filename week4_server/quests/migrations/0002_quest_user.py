# Generated by Django 3.1.5 on 2021-01-27 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to=settings.AUTH_USER_MODEL),
        ),
    ]
