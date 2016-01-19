__author__ = 'Administrator'
#coding=utf-8
from django.shortcuts import render_to_response,HttpResponse
from docker import Client


def image(request):

    cli =Client(base_url="tcp://s2.95xd.com:2375")
    images = cli.images()

    return render_to_response("image.html",{"images": images})

def build(request):
    tag = request.POST.get("tag",None)
    dockerfile = request.POST.get("dockerfile",None)
    from io import BytesIO
    print tag,dockerfile

    f = BytesIO(dockerfile.encode('utf-8'))
    cli = Client(base_url='tcp://s2.95xd.com:2375')
    response = cli.build(fileobj=f,rm=True,tag=tag)

    return HttpResponse(response)