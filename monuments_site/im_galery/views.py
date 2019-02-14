from django.shortcuts import render


def galery_render(request):
    images = None
    return render(request, 'galery.html', context={images})
