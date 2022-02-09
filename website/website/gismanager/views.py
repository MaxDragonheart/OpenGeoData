from django.shortcuts import render, get_object_or_404

from .models import WMSLayer


def wms_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = WMSLayer.objects.all()
    context = {"list": list}
    return render(request, "wms_list.html", context)