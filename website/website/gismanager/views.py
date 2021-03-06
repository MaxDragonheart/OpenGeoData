from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.db.models import Q

from itertools import chain

from .models import OGCLayer, Basemap, WebGISProject


# def test_map(request):
#     return render(request, "test/test_map.html")


# def test_map_single(request, id):
#     object = get_object_or_404(Basemap, id=id)
#
#     context = {
#         "single_object": object,
#     }
#     template = "test/test_map_single.html"
#     return render(request, template, context)


def search(request):
    template = "search_results.html"

    if "q" in request.GET:
        querystring = request.GET.get("q")
        wms = OGCLayer.objects.filter(
                                Q(title__icontains=querystring) |
                                Q(description__icontains=querystring)
                            )
        webgis = WebGISProject.objects.filter(
                                Q(title__icontains=querystring) |
                                Q(description__icontains=querystring)
                            )


        context = {
            "name": _("Risultati della ricerca"),
            "objects": list(chain(wms, webgis)),
        }
        return render(request, template, context)
    else:
        return render(request, template)


def wms_list(request):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of objects from OGCLayer Model.

    Args:
        request:

    Returns:
        JSON
    """
    list = OGCLayer.objects.all()
    context = {
        "name": _("Lista dei WMS"),
        "list": list
    }
    return render(request, "wms/wms_list.html", context)


def single_wms(request, slug):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from OGCLayer Model.

    Args:
        request:
        slug: String.

    Returns:
        JSON
    """
    object = get_object_or_404(OGCLayer, slug=slug)

    context = {
        "single_object": object,
    }
    template = "wms/single_wms.html"
    return render(request, template, context)


def webgis_list(request):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of objects from WebGISProject Model.

    Args:
        request:

    Returns:
        JSON
    """
    list = WebGISProject.objects.all()
    context = {
        "name": _("Lista delle mappe"),
        "list": list
    }
    return render(request, "webgis/webgis_list.html", context)


def single_webgis(request, slug):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from WebGISProject Model.

    Args:
        request:
        slug: String.

    Returns:
        JSON
    """
    object = get_object_or_404(WebGISProject, slug=slug)

    context = {
        "single_object": object,
    }
    template = "webgis/single_webgis.html"
    return render(request, template, context)
