# Generated by Django 5.0 on 2023-12-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='телеграм id'),
        ),
    ]