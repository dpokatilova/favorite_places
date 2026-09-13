from django.shortcuts import render
import random
from .data import FAVORITE_PLACES

def home_view(request):
    featured_place = None
    if FAVORITE_PLACES:
        weights = []
        for place in FAVORITE_PLACES:
            rating = place.get("rating", 1)
            weights.append(rating)

        featured_place = random.choices(FAVORITE_PLACES, weights=weights, k=1)[0]
    context = {
        "featured_place": featured_place
    }
    return render(request, "places/home.html", context)