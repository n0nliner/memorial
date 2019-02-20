from django.urls import path , include
from .views import *

urlpatterns = [
    path('', main_page , name='main_page_url'),
    path('main/', main_page , name='main_page_url'),
    path('data/', send_maiL, name="send_data_url")
]
