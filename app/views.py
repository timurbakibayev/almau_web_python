from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

cars = [
    {"model": "Toyota Camry", "speed": 220, "color": "red"},
    {"model": "Honda Civic", "speed": 120, "color": "blue"},
    {"model": "Tesla", "speed": 400, "color": "green"},
]


def show_cars(request: HttpRequest) -> HttpResponse:
    global cars
    return render(request, "cars.html", context={"cars": cars})
