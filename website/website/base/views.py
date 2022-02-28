from itertools import chain

from django.shortcuts import render, get_object_or_404

from .models import SharedCategories
from gismanager.models import OGCLayer, WebGISProject


def index(request):
    template = 'home/index.html'
    return render(request, template)


def sharedcategories_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = SharedCategories.objects.all()
    context = {"list": list}
    return render(request, "shared-categories/shared_categories_list.html", context)


def single_sharedcategory(request, slug):
    object = get_object_or_404(SharedCategories, slug=slug)
    wms = OGCLayer.objects.filter(categories=object)
    map = WebGISProject.objects.filter(categories=object)

    context = {
        "single_object": object,
        "objects": list(chain(wms, map))
    }
    template = "shared-categories/single_shared_categories.html"
    return render(request, template, context)