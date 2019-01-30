from django.shortcuts import render
from instruments.models import Guitar


def index(request):
    guitars = Guitar.objects.all()
    context = {
        'guitars': guitars,
    }
    return render(request, 'home/index.html', context)


def payment_methods(request):
    return render(request, 'home/payment_methods.html')
