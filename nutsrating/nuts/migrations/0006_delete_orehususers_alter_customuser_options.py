# Generated by Django 4.0.2 on 2022-03-23 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuts', '0005_alter_customuser_options_alter_customuser_birth_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrehusUsers',
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-rating'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
