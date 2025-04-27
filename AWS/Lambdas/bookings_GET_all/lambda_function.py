# /api/v1/bookings GET

from service.booking_service import BookingService

def lambda_handler(event, context):
    return BookingService().get_all_bookings()

print(lambda_handler(event=None, context=None))