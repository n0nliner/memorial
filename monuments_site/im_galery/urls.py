from django.urls import path , include
from .views import *


urlpatterns = [
    path('', galery_render , name='galery_url')
]
