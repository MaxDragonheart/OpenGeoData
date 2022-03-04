from django.conf import settings
from django.db import models
from django.utils import timezone

from bs4 import BeautifulSoup


def size(field):
    """Make comprensible the size of an object
    like a document(.pdf, .xls, etc..) or an
    image(.png, .jpg, etc..).

    Args:
        field: Model field name

    Returns:
        Number
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


# TODO Develop this function
# def extension(field):
#     """Get the extension from file.
#
#     :param field:
#     :return:
#     """
#
#     extension = ""
#     return extension


class TimeManager(models.Model):
    """
    TimeManager Abstract Model is useful to define when:
    - the object is created thanks to `timestamp` field;
    - the object is published thanks to `publishing_date` field;
    - the object is updated thanks to `updating_date` field.
    """
    publishing_date = models.DateTimeField(default=timezone.now)
    updating_date = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    @property
    def is_future(self):
        """Check if an object is published in the
        future or not.

        Returns:
            Boolean
        """
        if self.publishing_date > timezone.now():
            return True
        return False

    class Meta:
        abstract = True


class FileUploadBase(TimeManager):
    """
    FileUploadBase Abstract Model is used to give a name
    and a description for an uploaded object.
    """
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        """Delete related file when an object is deleted
        from a Model for upload the object.

        Args:
            *args:
            **kwargs:
        """
        self.file.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        abstract = True


class TagBase(TimeManager):
    """
    TagBase Abstract Model is used for
    create the tag.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class CategoryBase(TagBase):
    """
    CategoryBase Abstract Model is used for
    create the category.
    """
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BaseModelPost(TimeManager):
    """
    BaseModelPost Abstract Model is used for
    create a generic post.
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
    ModelPost Abstract Model expand BaseModelPost
    by adding more fields.
    """
    contents = models.TextField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

    @property
    def time_of_reading(self):
        """Count how much time it is necessary
        to read the post.

        Returns:
            Number
        """
        max_words = 200
        string = str(self.contents)
        cleantext = BeautifulSoup(string, "lxml").text
        timeofreading = int(len(cleantext.split()) / max_words)
        return timeofreading

    class Meta:
        abstract = True


class UrlsModel(TimeManager):
    """
    UrlsModel Abstract Model is used to give a name
    and an url for website url object.
    """
    name = models.CharField(max_length=70)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True