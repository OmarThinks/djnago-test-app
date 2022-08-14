from django.http import HttpResponse


def my_custom_not_found(request, *args, **kwargs):
    res = HttpResponse("404")
    res.status_code = 404
    return res