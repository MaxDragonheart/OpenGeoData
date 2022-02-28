from django.shortcuts import render, get_object_or_404

from .models import SharedCategories


def index(request):
    template = 'home/index.html'
    return render(request, template)


def sharedtag_list(request):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    list = SharedCategories.objects.all()
    context = {"list": list}
    return render(request, "shared-tags/sharedtags_list.html", context)


def single_shared(request, slug):
    object = get_object_or_404(SharedCategories, slug=slug)

    context = {
        "single_object": object,
    }
    template = "shared-tags/single_sharedtags.html"
    return render(request, template, context)