from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    print(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def thanks(request):
    return HttpResponse('Thank you')
