from django.db import models
from django.utils import timezone

import os
from bs4 import BeautifulSoup
from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField


class TimeManager(models.Model):
    """
    Definizione dello standard tempo
    """
    publishing_date = models.DateTimeField(default=timezone.now)
    updating_date = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    @property
    def is_future(self):
        """
        Funzione che verifica se un post è da pubblicare nel futuro o subito
        """
        if self.publishing_date > timezone.now():
            return True
        return False

    class Meta:
        abstract = True


class FileUploadBase(TimeManager):
    """
    Modello generico
    """
    name = models.CharField(
        max_length=70,
        )
    description = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        """
        Funzione che consente di cancellare un file caricato eliminando
        sia il path dal DB che il file in se dalla directory
        """
        self.file.delete()
        super().delete(*args, **kwargs)

    @property
    def size(self):
        """
        Funzione che umanizza le dimensioni di un file caricato
        """
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext

    @property
    def extension(self):
        """
        Funzione che estrae l'estensione di un file caricato
        """
        name, extension = os.path.splitext(self.file.name)
        return extension

    class Meta:
        ordering = ['-publishing_date']
        abstract = True


class FileBrowserFileUploadBase(TimeManager):
    """
    Modello generico
    """
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def size(self):
        """
        Funzione che umanizza le dimensioni di un file caricato
        ref: https://django-filebrowser.readthedocs.io/en/latest/fileobject.html
        """
        x = self.file.filesize
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext

    @property
    def extension(self):
        """
        Funzione che estrae l'estensione di un file caricato
        ref: https://django-filebrowser.readthedocs.io/en/latest/fileobject.html
        """
        return self.file.extension

    class Meta:
        ordering = ['-publishing_date']
        abstract = True


class CategoryBase(TimeManager):
    """
    definizione delle caratteristiche di una categoria
    """
    category_name = models.CharField(max_length=50, unique=True)
    slug_category = models.SlugField(unique=True)
    description = tinymce_models.HTMLField(blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        abstract = True


class TagBase(TimeManager):
    """
    definizione delle caratteristiche di un tag
    """
    tag_name = models.CharField(max_length=50, unique=True)
    slug_tag = models.SlugField(unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        abstract = True


class BaseModelPost(TimeManager):
    """
    Modello base per i post.
    """
    title = models.CharField(max_length=70, unique=True)
    slug_post = models.SlugField(max_length=70, unique=True)
    header_image = FileBrowseField(max_length=200, directory="images/", blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ModelPost(BaseModelPost):
    """
    Con questa classe definisco le caratteristiche
    comuni dei post
    """
    contents = tinymce_models.HTMLField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

    @property
    def time_of_reading(self):
        """
        Funzione che definisce il tempo di lettura.
        E' possibile leggere mediamente 200 parole al minuto.
        """
        max_words = 200
        string = str(self.contents)
        cleantext = BeautifulSoup(string, "lxml").text
        timeofreading = int(len(cleantext.split()) / max_words)
        return timeofreading

    class Meta:
        abstract = True