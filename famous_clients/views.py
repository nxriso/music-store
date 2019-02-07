from django.shortcuts import render
from famous_clients.models import FamousClients


def famous_customers(request):
    famous_customers = FamousClients.objects.all()
    context = {
        'famous_customers': famous_customers
    }
    return render(request, 'famous_clients/famous.html', context)
