# Generated by Django 4.0.2 on 2022-03-27 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuts', '0010_alter_customuser_user_zodiac_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_zodiac_sign',
        ),
    ]