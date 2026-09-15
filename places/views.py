from django.shortcuts import render, redirect
import random
from .data import FAVORITE_PLACES
from .forms import NewPlaceForm

def get_user_places(request):
    if "places" not in request.session:
        request.session["places"] = list(FAVORITE_PLACES)
    return request.session["places"]


def home_view(request):
    current_places = get_user_places(request)

    featured_place = None
    if request.GET.get("roll") == "true" and current_places:
        total_rating = 0
        for p in current_places:
            total_rating += int(p.get("rating", 1))
        random_point = random.randint(1, total_rating)

        current_sum = 0
        for p in current_places:
            current_sum += int(p.get("rating", 1))
            if current_sum >= random_point:
                featured_place = p
                break

    return render(request, "places/home.html", {"featured_place": featured_place})

def places_list_view(request):
    context = {
        "places": get_user_places(request)
    }
    return render(request, "places/places_list.html", context)


def place_detail_view(request, place_id):
    current_places = get_user_places(request)

    place = None
    for p in current_places:
        if p['id'] == place_id:
            place = p
            break

    if place is None:
        from django.http import Http404
        raise Http404("Місце не знайдено")

    return render(request, "places/place_detail.html", {"place": place})


def add_place_view(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            current_places = get_user_places(request)

            max_id = 0
            for p in current_places:
                if p["id"] > max_id:
                    max_id = p["id"]
            new_id = max_id + 1

            new_place = {
                "id": new_id,
                "title": form.cleaned_data['title'],
                "type": form.cleaned_data['place_type'],
                "location": form.cleaned_data['location'],
                "rating": form.cleaned_data['rating'],
                "long_description": form.cleaned_data['description'],
                "date_added": "2026-09-14",
            }
            current_places.append(new_place)
            request.session["places"] = current_places
            request.session.modified = True

            return redirect("places_list")
    else:
        form = NewPlaceForm()

    return render(request, 'places/add_place.html', {'form': form})
