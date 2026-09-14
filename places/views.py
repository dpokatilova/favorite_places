from django.shortcuts import render
import random
from .data import FAVORITE_PLACES
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewPlaceForm

def home_view(request):
    featured_place = None
    if request.GET.get("roll") and FAVORITE_PLACES:
        weights = []
        for place in FAVORITE_PLACES:
            rating = place.get("rating", 1)
            weights.append(rating)

        featured_place = random.choices(FAVORITE_PLACES, weights=weights, k=1)[0]
    context = {
        "featured_place": featured_place
    }
    return render(request, "places/home.html", context)


def places_list_view(request):
    context = {
        "places": FAVORITE_PLACES
    }
    return render(request, "places/places_list.html", context)


def place_detail_view(request, place_id):
    found_place = None
    for place in FAVORITE_PLACES:
        if place["id"] == place_id:
            found_place = place
            break

    context = {
        "place": found_place
    }
    return render(request, "places/place_detail.html", context)


def add_place_view(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            new_place = {
                "id": len(FAVORITE_PLACES) + 1,
                "title": form.cleaned_data['title'],
                "type": form.cleaned_data['place_type'],
                "location": form.cleaned_data['location'],
                "rating": form.cleaned_data['rating'],
                "description": form.cleaned_data['description'],
                "date_added": "2026-09-14",
            }
            FAVORITE_PLACES.append(new_place)
            return HttpResponseRedirect(reverse('places_list'))
    else:
        form = NewPlaceForm()

    return render(request, 'places/add_place.html', {'form': form})