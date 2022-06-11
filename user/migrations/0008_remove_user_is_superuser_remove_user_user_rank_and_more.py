# Generated by Django 4.0.5 on 2022-06-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_rank',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='이메일 주소'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60, verbose_name='비밀번호'),
        ),
    ]