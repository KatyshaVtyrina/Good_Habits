# Generated by Django 5.0 on 2023-12-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='признак публичности'),
        ),
    ]
