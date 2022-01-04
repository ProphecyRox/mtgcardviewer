from django.http import HttpResponse
from .models import Card
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .forms import SearchForm

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
    search_performed = False
    search_results = Card.objects.none()

    if request.method == "POST":
        # Process form data
        form = SearchForm(request.POST)
        if form.is_valid():
            # Get search results
            card_name = request.POST['name']
            search_results = Card.objects.filter(name__contains=card_name)
            # Set flag for template to use
            search_performed = True
    else:
        # Show blank form
        form = SearchForm()

    # Render form
    form_html = form.as_p()
    return render(request, 'viewer/search.html',
        {
            'form_html': form_html,
            'search_results': search_results,
            'search_performed': search_performed
        }
    )
