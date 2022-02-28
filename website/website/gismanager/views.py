from django.shortcuts import render, get_object_or_404

from .models import OGCLayer, Basemap, WebGISProject


def test_map(request):
    return render(request, "test/test_map.html")


def test_map_single(request, id):
    object = get_object_or_404(Basemap, id=id)

    context = {
        "single_object": object,
    }
    template = "test/test_map_single.html"
    return render(request, template, context)


def wms_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = OGCLayer.objects.all()
    context = {
        "name": "WMS List",
        "list": list
    }
    return render(request, "wms/wms_list.html", context)


def single_wms(request, slug):
    object = get_object_or_404(OGCLayer, slug=slug)

    context = {
        "single_object": object,
    }
    template = "wms/single_wms.html"
    return render(request, template, context)


def webgis_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = WebGISProject.objects.all()
    context = {
        "name": "Maps List",
        "list": list
    }
    return render(request, "map/webgis_list.html", context)


def single_webgis(request, slug):
    object = get_object_or_404(WebGISProject, slug=slug)

    context = {
        "single_object": object,
    }
    template = "map/single_webgis.html"
    return render(request, template, context)