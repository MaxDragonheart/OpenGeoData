# Generated by Django 4.0.2 on 2022-02-04 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_siteurls_sitecustomization_urls'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSocialUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updating_date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='sitecustomization',
            name='social_urls',
            field=models.ManyToManyField(related_name='related_sitesocialurls', to='base.SiteSocialUrls'),
        ),
    ]