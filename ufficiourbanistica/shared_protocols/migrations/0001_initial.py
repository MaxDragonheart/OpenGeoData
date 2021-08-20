# Generated by Django 3.2.6 on 2021-08-20 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SharedTag',
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
    ]
