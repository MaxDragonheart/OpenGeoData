# Generated by Django 4.0.2 on 2022-02-26 15:58
from django.db import migrations
from django.conf import settings

from ..utils import social_networks, categories


def set_first_url(apps, schema_editor):
    SiteUrls = apps.get_model('base', 'SiteUrls')
    SiteUrls.objects.create(
        name='null island website',
        url='http://www.null-island.null'
    )


def make_social_network_list(apps, schema_editor):
    SiteSocialUrls = apps.get_model('base', 'SiteSocialUrls')
    for social in social_networks:
        SiteSocialUrls.objects.create(
            name=social[0],
            url=social[1],
            icon=social[2],
        )


def make_site_description(apps, schema_editor):
    SiteCustomization = apps.get_model('base', 'SiteCustomization')

    if settings.DOMAIN_NAME:
        domain_name = settings.DOMAIN_NAME
    else:
        domain_name = 'null island website'

    if settings.DOMAIN:
        domain = settings.DOMAIN
    else:
        domain = 'www.nullisland.null'

    if settings.SITE_TITLE:
        site_title = settings.SITE_TITLE
    else:
        site_title = 'OpenGeoData'

    if settings.SITE_LOGO:
        site_logo = settings.SITE_LOGO
    else:
        site_logo = 'default/logo.png'

    if settings.SITE_DESCRIPTION:
        site_description = settings.SITE_DESCRIPTION
    else:
        site_description = 'Share GeoData to the World!'

    if settings.ADDRESS:
        address = settings.ADDRESS
    else:
        address = 'Geolocateme Correctly street, 1, Null Island, 9999888'

    if settings.CONTACT_PHONE:
        contact_phone = settings.CONTACT_PHONE
    else:
        contact_phone = '+39 0987543'

    if settings.CONTACT_EMAIL:
        contact_email = settings.CONTACT_EMAIL
    else:
        contact_email = 'mail@email.null'

    if settings.CONTACT_OFFICIAL_EMAIL:
        contact_official_email = settings.CONTACT_OFFICIAL_EMAIL
    else:
        contact_official_email = 'pec-mail@email.null'

    SiteCustomization.objects.create(
        name=domain_name,
        domain=domain,
        site_title=site_title,
        site_logo=site_logo,
        site_description=site_description,
        address=address,
        contact_phone=contact_phone,
        contact_email=contact_email,
        contact_official_email=contact_official_email,
    )


def make_default_sharedcategory(apps, schema_editor):
    SharedCategories = apps.get_model('base', 'SharedCategories')
    for category in categories:
        SharedCategories.objects.create(
            title=category[0],
            slug=category[1],
            icon=category[2],
            description=category[3]
        )


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_first_url),
        migrations.RunPython(make_social_network_list),
        migrations.RunPython(make_site_description),
        migrations.RunPython(make_default_sharedcategory)
    ]
