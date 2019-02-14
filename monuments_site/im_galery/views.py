from django.shortcuts import render
from .models import *

def galery_render(request):
    return render(request, 'galery.html', context={'photos':album.objects.all()})
