from .models import SiteCustomization


def site_customization(request):
    """Manage website description data.

    Args:
        request:

    Returns:
        JSON
    """
    data = SiteCustomization.objects.filter(id=1)
    protocol = request.scheme

    response = {
        'data': data,
        'protocol': protocol,
    }

    return response
