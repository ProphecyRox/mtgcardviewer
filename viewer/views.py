from django.http import HttpResponse
from .models import Card
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    first_five_cards = Card.objects.all()[:5]
    return render(request, 'viewer/index.html', {'first_five_cards': first_five_cards})

def details(request, id):
    try:
        card = Card.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Error 404: Card not found")

    return render(request, 'viewer/details.html', {'card': card})

def contact(request):
    return render(request, 'viewer/contact.html', {})

def search(request):
    return render(request, 'viewer/search.html', {})
