# /api/v1/cars GET

from service.cars_service import CarService

def lambda_handler(event, context):
    return CarService().get_all_cars()



