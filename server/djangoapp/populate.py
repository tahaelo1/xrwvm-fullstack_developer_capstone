from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "Toyota", "description": "Japanese multinational automotive manufacturer", "country": "Japan"},
        {"name": "Ford", "description": "American multinational automaker", "country": "USA"},
        {"name": "BMW", "description": "German multinational corporate manufacturer of luxury vehicles", "country": "Germany"},
        {"name": "Honda", "description": "Japanese public multinational conglomerate", "country": "Japan"},
        {"name": "Chevrolet", "description": "American automobile division of General Motors", "country": "USA"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make, created = CarMake.objects.get_or_create(name=data['name'], defaults=data)
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Camry", "type": "Sedan", "year": 2021, "car_make": car_make_instances[0]},
        {"name": "RAV4", "type": "SUV", "year": 2022, "car_make": car_make_instances[0]},
        {"name": "Mustang", "type": "Coupe", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "F-150", "type": "Truck", "year": 2022, "car_make": car_make_instances[1]},
        {"name": "3 Series", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "X5", "type": "SUV", "year": 2022, "car_make": car_make_instances[2]},
        {"name": "Civic", "type": "Sedan", "year": 2021, "car_make": car_make_instances[3]},
        {"name": "CR-V", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Silverado", "type": "Truck", "year": 2022, "car_make": car_make_instances[4]},
        {"name": "Equinox", "type": "SUV", "year": 2021, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(name=data['name'], car_make=data['car_make'], defaults=data)

    print("Data populated successfully!")