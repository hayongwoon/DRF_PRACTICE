# Generated by Django 4.0.5 on 2022-06-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_rank',
            field=models.IntegerField(default=1, verbose_name='회원 등급'),
        ),
    ]
