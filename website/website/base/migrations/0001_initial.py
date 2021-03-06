# Generated by Django 4.0.3 on 2022-04-10 17:57

import django.contrib.sites.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SharedCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SiteSocialUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=70)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SiteUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=70)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SiteCustomization',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sites.site')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('site_title', models.CharField(blank=True, default='OpenGeoData', max_length=250, null=True)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('site_description', models.CharField(blank=True, default='We share geodata', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='Geolocateme Correctly street, 1, - Null Island, 9999888', null=True)),
                ('contact_phone', models.CharField(blank=True, default='+39 0987543', max_length=250, null=True)),
                ('contact_email', models.EmailField(blank=True, default='mail@email.null', max_length=254, null=True)),
                ('contact_official_email', models.EmailField(blank=True, default='pec-mail@email.null', max_length=254, null=True)),
                ('urls', models.ManyToManyField(related_name='related_siteurls', to='base.siteurls')),
            ],
            options={
                'verbose_name': 'Customize site',
                'verbose_name_plural': 'Customize site',
            },
            bases=('sites.site', models.Model),
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
