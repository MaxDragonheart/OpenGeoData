from itertools import chain

from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _

from .models import SharedCategories, Organogram
from gismanager.models import OGCLayer, WebGISProject

# def index(request):
#     template = 'home/index.html'
#     return render(request, template)


def sharedcategories_list(request):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of objects from SharedCategories Model.


    Args:
        request:

    Returns:
        JSON
    """
    list = SharedCategories.objects.all()
    context = {
        "name": _("lista"),
        "list": list,
    }
    return render(request, "shared-categories/shared_categories_list.html", context)


def single_sharedcategory(request, slug):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from SharedCategories Model.

    Args:
        request:
        slug: String.

    Returns:
        JSON
    """
    object = get_object_or_404(SharedCategories, slug=slug)
    wms = OGCLayer.objects.filter(categories=object)
    webgis = WebGISProject.objects.filter(categories=object)

    context = {
        "single_object": object,
        "objects": list(chain(wms, webgis)),
    }
    template = "shared-categories/single_shared_categories.html"
    return render(request, template, context)


def organogram(request):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from Organogram Model.

    Args:
        request:
        slug: String.

    Returns:
        JSON
    """
    data = Organogram.objects.all()
    if data:
        context = {
            "contents": data[0],
        }
    else:
        context = {
            "contents": _("Aggiungi contenuti"),
        }
    template = "organogram.html"
    return render(request, template, context)
