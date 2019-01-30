from django.shortcuts import render
from instruments.models import Guitar


def all_guitars(request):
    guitars = Guitar.objects.all()
    context = {
        'guitars': guitars,
    }
    return render(request, 'instruments/all_guitars.html', context)


def show_details(request, guitar_id):
    guitar = Guitar.objects.get(pk=guitar_id)
    context = {
        'guitar': guitar
    }
    return render(request, 'instruments/guitar_details.html', context)
