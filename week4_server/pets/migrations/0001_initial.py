# Generated by Django 3.1.5 on 2021-01-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('BIRD', 'BIRD'), ('CAT', 'CAT'), ('CHICKEN', 'CHICKEN'), ('COW', 'COW'), ('DOG', 'DOG'), ('DUCK', 'DUCK'), ('ELEPHANT', 'ELEPHANT'), ('KOALA', 'KOALA'), ('LLAMA', 'LLAMA'), ('PENGUIN', 'PENGUIN')], default='DOG', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
