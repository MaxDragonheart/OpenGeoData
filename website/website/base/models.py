from django.db import models
from django.urls import reverse

from abstracts.models import TagBase


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
