# Generated by Django 4.0.2 on 2022-02-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0021_alter_webgisproject_layers'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmslayer',
            name='wms_legend',
            field=models.BooleanField(default=False),
        ),
    ]