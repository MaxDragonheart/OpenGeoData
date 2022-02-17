# Generated by Django 4.0.2 on 2022-02-17 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gismanager', '0018_alter_webgisproject_basemap2'),
    ]

    operations = [
        migrations.AddField(
            model_name='webgisproject',
            name='main_layer',
            field=models.ForeignKey(default=34, on_delete=django.db.models.deletion.PROTECT, related_name='related_mainlayer', to='gismanager.wmslayer'),
            preserve_default=False,
        ),
    ]