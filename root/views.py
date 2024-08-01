from django.shortcuts import render
from .models import Serivces


def home(request):
    services=Serivces.object.filter(status=True)
    return render(request,'root/index.html',context={'services':Serivces})
