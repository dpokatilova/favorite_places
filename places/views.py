from django.shortcuts import render
import random
from .data import FAVORITE_PLACES

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
