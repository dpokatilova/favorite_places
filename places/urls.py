from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name= "home"),
    path("places/", views.places_list_view, name="places_list"),
    path("places/<int:place_id>/", views.place_detail_view, name="place_detail")
]