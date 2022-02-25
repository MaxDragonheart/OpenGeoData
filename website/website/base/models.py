from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site

from abstracts.models import TagBase, TimeManager, FileUploadBase, UrlsModel


social = {
    "facebook": '<i class="fab fa-facebook-f"></i>',
    "linkedin": '<i class="fab fa-linkedin-in"></i>',
    "instagram": '<i class="fab fa-instagram"></i>',
    "youtube": '<i class="fab fa-youtube"></i>',
}


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


class SiteUrls(UrlsModel):

    class Meta:
        ordering = ['name']
        verbose_name = "Url"
        verbose_name_plural = "Urls"


class SiteSocialUrls(UrlsModel):

    @property
    def social_icon(self):
        get_social = self.name.lower()
        if get_social in social:
            return social[get_social]
        else:
            return f"{get_social} is not accepted! If it is a social add to `social` dict to see the icon."

    class Meta:
        ordering = ['name']
        verbose_name = "Social"
        verbose_name_plural = "Social"


class SiteCustomization(TimeManager):
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name="related_sitecustomization")
    site_title = models.CharField(max_length=250, blank=True, null=True, default="OpenGeoData")
    site_logo = models.ImageField(upload_to=settings.UPLOADED_IMAGE_FOLDER, blank=True, null=True)
    site_description = models.CharField(max_length=100, blank=True, null=True, default="We share geodata")
    address = models.TextField(blank=True, null=True, default="Geolocateme Correctly street, 1, - Null Island, 9999888")
    contact_phone = models.CharField(max_length=250, blank=True, null=True, default="+39 0987543")
    contact_email = models.EmailField(blank=True, null=True, default="mail@email.null")
    contact_official_email = models.EmailField(blank=True, null=True, default="pec-mail@email.null")
    urls = models.ManyToManyField(SiteUrls, related_name="related_siteurls")
    #social_urls = models.ManyToManyField(SiteSocialUrls, related_name="related_sitesocialurls")

    def __str__(self):
        return self.site.name

    class Meta:
        verbose_name = "Dettagli del sito"
        verbose_name_plural = "Dettagli del sito"