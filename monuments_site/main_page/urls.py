from django.urls import path , include
from .views import *

urlpatterns = [
    path('', main_page , name='main_page_url')
]
