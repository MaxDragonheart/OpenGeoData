from django.shortcuts import render, get_object_or_404

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


def wms_list(request):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of objects from OGCLayer Model.

    :param request:
    :return: JSON
    """
    list = OGCLayer.objects.all()
    context = {
        "name": "WMS List",
        "list": list
    }
    return render(request, "wms/wms_list.html", context)


def single_wms(request, slug):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from OGCLayer Model.

    :param request:
    :param slug:
    :return: JSON
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

    :param request:
    :return: JSON
    """
    list = WebGISProject.objects.all()
    context = {
        "name": "Maps List",
        "list": list
    }
    return render(request, "webgis/webgis_list.html", context)


def single_webgis(request, slug):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from WebGISProject Model.

    :param request:
    :param slug:
    :return: JSON
    """
    object = get_object_or_404(WebGISProject, slug=slug)

    context = {
        "single_object": object,
    }
    template = "webgis/single_webgis.html"
    return render(request, template, context)