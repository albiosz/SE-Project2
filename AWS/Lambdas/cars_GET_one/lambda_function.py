# /api/v1/cars/{car_id} GET

from exceptions.cars_exceptions import InvalidCarIdException
from service.cars_service import CarService

def lambda_handler(event, context):
    car_id = event.get('car_id')
    if car_id is None or not car_id.isnumeric():
        raise InvalidCarIdException(car_id)
    else:
        return CarService().get_car_by_id(int(car_id))


