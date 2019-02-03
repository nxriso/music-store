from django.shortcuts import render
from instruments.models import Guitar
from instruments.models import Brand
from django.shortcuts import get_object_or_404


def all_brands(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'instruments/all_brands.html', context)


def guitars(request, brand_name):
    brand = get_object_or_404(Brand, name=brand_name)

    guitars = Guitar.objects.filter(brand__name=brand.name)
    context = {
        'guitars': guitars,
    }
    return render(request, 'instruments/all_guitars.html', context)


def show_details(request, guitar_model_name, brand_name):
    guitar = Guitar.objects.get(model_name=guitar_model_name, brand__name=brand_name)
    context = {
        'guitar': guitar
    }
    return render(request, 'instruments/guitar_details.html', context)
