from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import random

cars = [
    {"id": 1, "model": "Toyota Camry", "speed": 220, "color": "red"},
    {"id": 2, "model": "Honda Civic", "speed": 120, "color": "blue"},
    {"id": 3, "model": "Tesla", "speed": 400, "color": "green"},
]


def show_cars(request: HttpRequest) -> HttpResponse:
    global cars
    return render(request, "cars.html", context={"cars": cars})


def delete_car(request: HttpRequest, id_: int) -> HttpResponse:
    global cars
    new_cars = []
    for car in cars:
        if car["id"] != id_:
            new_cars.append(car)
    cars = new_cars
    return redirect("/cars")


def add_car(request: HttpRequest) -> HttpResponse:
    global cars
    last_id = 0
    if len(cars):
        last_id = cars[-1]["id"]
    new_car = {
        "id": last_id + 1,
        "model": random.choice([
            "Toyota", "Porsche", "Mercedes", "Audi", "Mazda", "Lexus",
        ]),
        "speed": random.randint(10, 20) * 10,
        "color": random.choice([
            "red", "blue", "white", "purple", "green", "violet",
        ]),
    }
    cars.append(new_car)
    return redirect("/cars")
