from django.db import models
from django.urls import reverse

from abstracts.models import CategoryBase, ModelPost

from shared_protocols.models import SharedTag


class ProtezioneCivileCategorie(CategoryBase):
    """
    Questa classe definisce le caratteristiche di
    una categoria
    """

    def get_absolute_url(self):
        return reverse("single_protezionecivilecategoria", kwargs={"slug_category": self.slug_category})

    class Meta:
        ordering = ['category_name']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"


class ProtezioneCivileContenuti(ModelPost):
    """
    Questa classe definisce le caratteristiche di
    un contenuto
    """
    category = models.ForeignKey(ProtezioneCivileCategorie, on_delete=models.PROTECT, related_name="related_protezionecivilecategoria")
    protezione_civile_sharedtags = models.ManyToManyField(SharedTag, related_name="related_protezionecivile_sharedtag")

    def get_absolute_url(self):
        return reverse("single_contenuto", kwargs={
                                                "slug_post": self.slug_post,
                                                "slug_category": self.category.slug_category,
                                                })

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Contenuto"
        verbose_name_plural = "Contenuti"