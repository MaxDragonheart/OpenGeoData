# Generated by Django 4.0.2 on 2022-02-03 14:12

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
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documenti',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SharedTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag_name', models.CharField(max_length=50, unique=True)),
                ('slug_tag', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Tag Condivso',
                'verbose_name_plural': 'Tag Condivisi',
                'ordering': ['tag_name'],
            },
        ),
        migrations.CreateModel(
            name='SiteCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('site_title', models.CharField(blank=True, default='Gestione del Territorio', max_length=250, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_sitecustomization', to='sites.site')),
            ],
            options={
                'verbose_name': 'Dettagli del sito',
                'verbose_name_plural': 'Dettagli del sito',
            },
        ),
    ]
