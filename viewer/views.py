from django.http import HttpResponse
from .models import Card
from django.template import loader #, render

def index(request):
    first_five_cards = Card.objects.all()[:5]
    template = loader.get_template('viewer/index.html')
    context = {
        'first_five_cards': first_five_cards
    }
    return HttpResponse(template.render(context, request))

def details(request, name):
    template = loader.get_template('viewer/details.html')
    context = {
        'name': name,
    }
    return HttpResponse(template.render(context, request))