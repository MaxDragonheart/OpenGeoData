# Generated by Django 4.0.2 on 2022-02-16 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0013_webgisproject_basemap1_webgisproject_basemap2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webgisproject',
            name='basemap1',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_basemap1', to='gismanager.basemap'),
        ),
    ]
