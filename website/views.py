from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def error404(request):
    template = loader.get_template('home/404.htm')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)
