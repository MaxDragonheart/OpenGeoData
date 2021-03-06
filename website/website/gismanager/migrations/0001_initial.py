# Generated by Django 4.0.3 on 2022-04-10 17:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basemap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('tile_code', models.CharField(blank=True, max_length=250, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Basemap',
                'verbose_name_plural': 'Basemaps',
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='BasemapProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('user', models.CharField(blank=True, max_length=250, null=True)),
                ('token', models.CharField(blank=True, max_length=250, null=True)),
                ('raw_url', models.TextField()),
            ],
            options={
                'verbose_name': 'Basemap Provider',
                'verbose_name_plural': 'Basemap Provider',
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='GeoServerURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('geoserver_domain', models.URLField(unique=True)),
                ('geoserver_workspace', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Geoserver url',
                'verbose_name_plural': 'Geoserver urls',
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='OGCLayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('map_scaleline', models.BooleanField(default=True)),
                ('map_attribution', models.CharField(default='<a href="https://massimilianomoraca.it/" target="_blank">Massimiliano Moraca</a> has created this map using <a href="https://openlayers.org/" target="_blank">OpenLayers</a>', max_length=250)),
                ('map_center_longitude', models.DecimalField(decimal_places=5, default=14.23964, max_digits=10)),
                ('map_center_latitude', models.DecimalField(decimal_places=5, default=40.8429, max_digits=10)),
                ('set_max_zoom', models.IntegerField(default=28)),
                ('set_min_zoom', models.IntegerField(default=0)),
                ('set_zoom_level', models.IntegerField(default=0)),
                ('set_zindex', models.IntegerField(default=1)),
                ('set_opacity', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('ogc_layer_name', models.CharField(max_length=100)),
                ('ogc_layer_style', models.CharField(blank=True, max_length=100, null=True)),
                ('ogc_bbox', models.CharField(blank=True, max_length=250, null=True)),
                ('ogc_centroid', models.CharField(blank=True, max_length=250, null=True)),
                ('ogc_legend', models.BooleanField(default=False)),
                ('is_vector', models.BooleanField()),
                ('is_raster', models.BooleanField()),
                ('categories', models.ManyToManyField(related_name='related_ogc_categories', to='base.sharedcategories')),
                ('ogc_layer_path', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_geoserver_url', to='gismanager.geoserverurl')),
            ],
            options={
                'verbose_name': 'OGC Layer',
                'verbose_name_plural': 'OGC Layers',
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='WebGISProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('contents', models.TextField(blank=True, null=True)),
                ('draft', models.BooleanField(default=False)),
                ('highlighted', models.BooleanField(default=False)),
                ('map_scaleline', models.BooleanField(default=True)),
                ('map_attribution', models.CharField(default='<a href="https://massimilianomoraca.it/" target="_blank">Massimiliano Moraca</a> has created this map using <a href="https://openlayers.org/" target="_blank">OpenLayers</a>', max_length=250)),
                ('map_center_longitude', models.DecimalField(decimal_places=5, default=14.23964, max_digits=10)),
                ('map_center_latitude', models.DecimalField(decimal_places=5, default=40.8429, max_digits=10)),
                ('set_max_zoom', models.IntegerField(default=28)),
                ('set_min_zoom', models.IntegerField(default=0)),
                ('set_zoom_level', models.IntegerField(default=0)),
                ('basemap1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_basemap1', to='gismanager.basemap')),
                ('basemap2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_basemap2', to='gismanager.basemap')),
                ('basemap3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_basemap3', to='gismanager.basemap')),
                ('categories', models.ManyToManyField(related_name='related_webgisproject_categories', to='base.sharedcategories')),
                ('layers', models.ManyToManyField(blank=True, related_name='related_wmslayer', to='gismanager.ogclayer')),
                ('main_layer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_main_wmslayer', to='gismanager.ogclayer')),
            ],
            options={
                'verbose_name': 'WebGIS',
                'verbose_name_plural': 'WebGIS',
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.AddField(
            model_name='basemap',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releted_basemap_provider', to='gismanager.basemapprovider'),
        ),
    ]
