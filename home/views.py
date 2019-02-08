from django.shortcuts import render

from instruments.models import Guitar
from famous_clients.models import FamousClients


def index(request):
    guitars = Guitar.objects.all()
    famous_customers = FamousClients.objects.all()
    featured_customers = FamousClients.objects.filter(featured=True)
    context = {
        'guitars': guitars,
        'famous_customers': famous_customers,
        'featured_customers': featured_customers,
    }
    return render(request, 'home/index.html', context)


def payment_methods(request):
    return render(request, 'home/payment_methods.html')
