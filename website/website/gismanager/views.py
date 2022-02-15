from django.shortcuts import render, get_object_or_404

from .models import WMSLayer, Basemap


def test_map(request):
    return render(request, "test/test_map.html")


def test_map_single(request, pk):
    object = get_object_or_404(WMSLayer, pk=pk)

    context = {
        "single_object": object,
    }
    template = "test/test_map_single.html"
    return render(request, template, context)


def wms_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = WMSLayer.objects.all()
    context = {"list": list}
    return render(request, "wms_list.html", context)


def single_wms(request, slug_post):
    object = get_object_or_404(WMSLayer, slug_post=slug_post)

    context = {
        "single_object": object,
    }
    template = "single_wms.html"
    return render(request, template, context)
