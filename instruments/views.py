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


def guitars(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)

    guitars = Guitar.objects.filter(brand__slug=brand.slug)
    context = {
        'guitars': guitars,
    }
    return render(request, 'instruments/all_guitars.html', context)


def show_details(request, guitar_slug, brand_slug):
    guitar = Guitar.objects.get(
        slug=guitar_slug, brand__slug=brand_slug
    )
    context = {
        'guitar': guitar
    }
    return render(request, 'instruments/guitar_details.html', context)
