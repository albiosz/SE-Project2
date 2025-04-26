# /api/v1/bookings GET

from package.exceptions.bookings_exceptions import *

from package.service.booking_service import get_all_bookings

def lambda_handler(event, context):
    try:
        return get_all_bookings()
    except ServiceUnavailableException as e:
        return None