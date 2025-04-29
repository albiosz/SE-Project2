# /api/v1/bookings/{booking_id} GET
from exceptions.bookings_exceptions import InvalidBookingIdException
from service.booking_service import BookingService

def lambda_handler(event, context):
    booking_id = event.get('booking_id')
    if booking_id is None or not booking_id.isnumeric():
        raise InvalidBookingIdException(booking_id)
    else:
        return BookingService().get_booking_by_id(int(booking_id))


