# Generated by Django 5.0 on 2023-12-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(verbose_name='время'),
        ),
    ]