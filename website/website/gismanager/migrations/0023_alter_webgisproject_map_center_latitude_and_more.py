# Generated by Django 4.0.2 on 2022-02-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0022_wmslayer_wms_legend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webgisproject',
            name='map_center_latitude',
            field=models.DecimalField(decimal_places=5, default=40.8429, max_digits=10),
        ),
        migrations.AlterField(
            model_name='webgisproject',
            name='map_center_longitude',
            field=models.DecimalField(decimal_places=5, default=14.23964, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wmslayer',
            name='map_center_latitude',
            field=models.DecimalField(decimal_places=5, default=40.8429, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wmslayer',
            name='map_center_longitude',
            field=models.DecimalField(decimal_places=5, default=14.23964, max_digits=10),
        ),
    ]
