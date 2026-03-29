from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


cars = [
    {"id": 1, "brand": "Chevrolet", "model": "Gentra", "year": 2023},
    {"id": 2, "brand": "Tesla", "model": "Model S", "year": 2024},
    {"id": 3, "brand": "BMW", "model": "M5 F90", "year": 2022},
    {"id": 4, "brand": "Toyota", "model": "Camry 75", "year": 2021}
]


# for car in cars:
#     print(f"{car['brand']} {car['model']} ({car['year']})")


def home(request: HttpRequest):
    contex = {
        'cars': cars
    }
    return render(request, 'main/index.html', contex)


def car_detail(request, car_id):
    for car in cars:
        if car.get('id') == car_id:
            contex = {
                'car': car
            }
            return render(request, 'main/detail.html', contex)
    return HttpResponse('Car not found', status=404)


def about(request: HttpRequest):
    return render(request, 'main/about.html')
