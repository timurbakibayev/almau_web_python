from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from app.models import Car
import random


def show_cars(request: HttpRequest) -> HttpResponse:
    cars = Car.objects.all()
    return render(request, "cars.html", context={"cars": cars})


def delete_car(request: HttpRequest, id_: int) -> HttpResponse:
    Car.objects.filter(pk=id_).delete()
    return redirect("/cars")


def add_car_random(request: HttpRequest) -> HttpResponse:
    Car.objects.create(
        model = random.choice([
            "Toyota", "Porsche", "Mercedes", "Audi", "Mazda", "Lexus",
        ]),
        speed = random.randint(10, 20) * 10,
        color = f"rgb({random.randint(0,255)},"
                f"{random.randint(0,255)},"
                f"{random.randint(0,255)})",
    )
    return redirect("/cars")


def add_new_car(request: HttpRequest) -> HttpResponse:
    error = ""
    default_model = ""
    default_speed = ""
    default_color = ""
    if request.method == "POST":
        speed = request.POST["speed"]
        default_model = request.POST["model"]
        default_speed = request.POST["speed"]
        default_color = request.POST["color"]
        if speed == "":
            error = "Please enter speed"
        if request.POST["model"] == "":
            error = "Please enter model"
        if error == "":
            Car.objects.create(
                model=request.POST["model"],
                speed=int(speed),
                color=request.POST["color"],
            )
            return redirect("/cars")
    return render(request, "car_new.html", context={
        "error": error,
        "defaul_model": default_model,
        "defaul_speed": default_speed,
        "defaul_color": default_color,
    })
