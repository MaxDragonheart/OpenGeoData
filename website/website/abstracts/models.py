from django.conf import settings
from django.db import models
from django.utils import timezone

from bs4 import BeautifulSoup


def size(field):
    """Funzione che umanizza le dimensioni di un file caricato

    :param field: Field name
    :return: f"{value} {unit}"
    """
    x = field.size
    y = 512000
    if x < y:
        value = round(x / 1000, 2)
        unit = ' kb'
    elif x < y * 1000:
        value = round(x / 1000000, 2)
        unit = ' Mb'
    else:
        value = round(x / 1000000000, 2)
        unit = ' Gb'
    return f"{value} {unit}"


def extension(field):
    """Funzione che estrae l'estensione di un file caricato

    :param field:
    :return:
    """
    # TODO sviluppare la funzione
    extension = ""
    return extension


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

    class Meta:
        ordering = ['-publishing_date']
        abstract = True


class CategoryBase(TimeManager):
    """
    definizione delle caratteristiche di una categoria
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class TagBase(TimeManager):
    """
    definizione delle caratteristiche di un tag
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BaseModelPost(TimeManager):
    """
    Modello base per i post.
    """
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    header_image = models.ImageField(upload_to=settings.UPLOADED_IMAGE_FOLDER, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ModelPost(BaseModelPost):
    """
    Con questa classe definisco le caratteristiche
    comuni dei post
    """
    contents = models.TextField(blank=True, null=True)
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


class UrlsModel(TimeManager):
    name = models.CharField(max_length=70)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True