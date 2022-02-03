from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site

from abstracts.models import TagBase, TimeManager, FileUploadBase


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


class SharedTags(TagBase):
    """
    Questa classe definisce le caratteristiche di
    un tag condiviso.
    """
    def get_absolute_url(self):
        return reverse("single_sharedtag", kwargs={"slug_tag": self.slug_tag})

    class Meta:
        ordering = ['tag_name']
        verbose_name = "Tag Condivso"
        verbose_name_plural = "Tag Condivisi"


class SiteCustomization(Site, TimeManager):
    site_title = models.CharField(max_length=250, blank=True, null=True, default="Gestione del Territorio")
    logo = models.ImageField(upload_to=settings.UPLOADED_IMAGE_FOLDER, blank=True, null=True)

    class Meta:
        verbose_name = "Dettagli del sito"
        verbose_name_plural = "Dettagli del sito"