# Generated by Django 4.0.2 on 2022-03-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuts', '0013_customuser_user_zodiac'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userzodiacsign',
            options={'verbose_name': 'Знак зодиака'},
        ),
        migrations.RenameField(
            model_name='userzodiacsign',
            old_name='user_zodiac',
            new_name='zodiac_sign',
        ),
    ]