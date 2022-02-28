from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site

from abstracts.models import CategoryBase, TimeManager, FileUploadBase, UrlsModel


class FileUpload(FileUploadBase):
    """
    Modello per l'upload di un file
    """
    file = models.FileField(upload_to=settings.UPLOADED_DOCUMENT_FOLDER, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("single_file", kwargs={"pk": self.pk})

    @property
    def url_path(self):
        return self.file.name

    class Meta:
        ordering = ['name']
        verbose_name = "Documento"
        verbose_name_plural = "Documenti"


class SharedCategories(CategoryBase):
    """
    Questa classe definisce le caratteristiche di
    un tag condiviso.
    """
    icon = models.ImageField(upload_to=settings.UPLOADED_IMAGE_FOLDER, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("single-sharedcategory", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"


class SiteUrls(UrlsModel):

    class Meta:
        ordering = ['name']
        verbose_name = "Url"
        verbose_name_plural = "Urls"


class SiteSocialUrls(UrlsModel):

    icon = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = "Social"
        verbose_name_plural = "Social"


class SiteCustomization(Site, TimeManager):
    site_title = models.CharField(max_length=250, blank=True, null=True, default="OpenGeoData")
    site_logo = models.ImageField(upload_to=settings.UPLOADED_IMAGE_FOLDER, blank=True, null=True)
    site_description = models.CharField(max_length=100, blank=True, null=True, default="We share geodata")
    address = models.TextField(blank=True, null=True, default="Geolocateme Correctly street, 1, - Null Island, 9999888")
    contact_phone = models.CharField(max_length=250, blank=True, null=True, default="+39 0987543")
    contact_email = models.EmailField(blank=True, null=True, default="mail@email.null")
    contact_official_email = models.EmailField(blank=True, null=True, default="pec-mail@email.null")
    urls = models.ManyToManyField(SiteUrls, related_name="related_siteurls")

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = "Dettagli del sito"
        verbose_name_plural = "Dettagli del sito"