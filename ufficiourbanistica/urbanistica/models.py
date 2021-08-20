from django.db import models
from django.urls import reverse

from abstracts.models import CategoryBase, ModelPost

from shared_protocols.models import SharedTag


class UrbanisticaCategorie(CategoryBase):
    """
    Questa classe definisce le caratteristiche di
    una categoria
    """

    def get_absolute_url(self):
        return reverse("single_urbanisticacategoria", kwargs={"slug_category": self.slug_category})

    class Meta:
        ordering = ['category_name']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"


class UrbanisticaContenuti(ModelPost):
    """
    Questa classe definisce le caratteristiche di
    un contenuto
    """
    category = models.ForeignKey(UrbanisticaCategorie, on_delete=models.PROTECT, related_name="related_urbanisticacategoria")
    urbanistica_sharedtags = models.ManyToManyField(SharedTag, related_name="related_urbanistica_sharedtag")

    def get_absolute_url(self):
        return reverse("single_contenuto", kwargs={
                                                "slug_post": self.slug_post,
                                                "slug_category": self.category.slug_category,
                                                })

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Contenuto"
        verbose_name_plural = "Contenuti"