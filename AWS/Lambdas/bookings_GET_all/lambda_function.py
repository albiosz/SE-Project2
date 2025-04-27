# /api/v1/bookings GET

from package.service.booking_service import get_all_bookings

def lambda_handler(event, context):
    return get_all_bookings()
