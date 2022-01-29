from django.shortcuts import render


def index(request):
    template = 'home/index.html'
    return render(request, template)