# Generated by Django 4.0.2 on 2022-02-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_sitesocialurls_icon_alter_sitesocialurls_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitecustomization',
            name='social_urls',
        ),
    ]
