# Generated by Django 5.0 on 2023-12-08 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место выполнения привычки')),
                ('time', models.DateTimeField(verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_pleasant', models.BooleanField(verbose_name='признак приятной привычки')),
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='периодичность в днях')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение')),
                ('time_to_complete', models.TimeField(verbose_name='время на выполнение привычки')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
