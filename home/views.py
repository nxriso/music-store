from django.shortcuts import render

from famous_clients.models import FamousClients
from instruments.models import Guitar
from .models import HomeSlide


def index(request):
    guitars = Guitar.objects.all()
    featured_customers = FamousClients.objects.filter(featured=True)
    featured_guitars = Guitar.objects.filter(featured=True)
    slide = HomeSlide.objects.all()

    context = {
        'guitars': guitars,
        'featured_customers': featured_customers,
        'featured_guitars': featured_guitars,
        'slide': slide,
    }
    return render(request, 'home/index.html', context)


def payment_methods(request):
    return render(request, 'home/payment_methods.html')
