from django.shortcuts import HttpResponse
from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    ip = request.environ.get('REMOTE_ADDR', None)
    web_user, created = WebUser.objects.get_or_create(ip=ip)
    if not created:
        web_user.pv += 1
        web_user.save()

    return render(request, '2.html', {'data': web_user})
