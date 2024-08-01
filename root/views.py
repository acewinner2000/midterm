from django.shortcuts import render
from .models import *


def home(request):
    services=Services.objects.filter(status=True)
    return render(request,'root/index.html' , context={'services' : services})
