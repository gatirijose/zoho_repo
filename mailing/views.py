from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 
# Create your views here.


def index(request):
    if request.method == 'POST':
        subject = 'Trial and Error'
        message  = request.POST['message']
        receiver = ['gatirijose@gmail.com',]

        send_mail(subject, message, receiver)
    return render(request, 'index.html')