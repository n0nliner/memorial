from django.shortcuts import render , redirect , HttpResponse
from django.core.mail import send_mail , EmailMessage
import smtplib


def main_page(request):
    return render(request, 'main_page.html')


def send_maiL(request):
    body = 'телефон {}\n имя {}\n фамилия {}'.format(str(request.POST['phone']), str(request.POST['name']), str(request.POST['surename']))
    msg = EmailMessage('work', body, 'neir0@outlook.com')
    return render(request, 'seccess.html')
