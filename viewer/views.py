from django.http import HttpResponse
from .models import Card
from django.template import loader #, render
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    first_five_cards = Card.objects.all()[:5]
    template = loader.get_template('viewer/index.html')
    context = {
        'first_five_cards': first_five_cards
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('viewer/details.html')
    try:
        card = Card.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Error 404: Card not found")

    context = {
        'card': card,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('viewer/contact.html')
    return HttpResponse(template.render({}, request))

def search(request):
    template = loader.get_template('viewer/search.html')
    return HttpResponse(template.render({}, request))
