# Generated by Django 5.0.4 on 2024-04-13 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]