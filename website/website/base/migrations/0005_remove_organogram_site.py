# Generated by Django 4.0.3 on 2022-05-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_organogram_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organogram',
            name='site',
        ),
    ]
