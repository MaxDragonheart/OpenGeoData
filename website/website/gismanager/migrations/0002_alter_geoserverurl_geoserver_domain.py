# Generated by Django 4.0.3 on 2022-05-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoserverurl',
            name='geoserver_domain',
            field=models.CharField(max_length=10000, unique=True),
        ),
    ]
