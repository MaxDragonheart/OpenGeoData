# Generated by Django 4.0.2 on 2022-02-15 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0009_remove_webgisproject_map_layers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webgisproject',
            name='basemap',
        ),
        migrations.RemoveField(
            model_name='webgisproject',
            name='basemap_layers',
        ),
    ]