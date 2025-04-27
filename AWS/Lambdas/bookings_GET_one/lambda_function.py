# /api/v1/bookings/{booking_id} GET

from package.service.booking_service import get_booking_by_id

def lambda_handler(event, context):
    booking_id = event.get('booking_id')
    return get_booking_by_id(booking_id)