# /api/v1/cars GET
from exceptions.cars_exceptions import InvalidCarIdException
from service.cars_service import CarService

def lambda_handler(event, context):
    booking_id = event.get('booking_id')
    if booking_id is None or not booking_id.isnumeric():
        raise InvalidCarIdException(booking_id)
    else:
        return CarService().get_booking_by_id(int(booking_id))


