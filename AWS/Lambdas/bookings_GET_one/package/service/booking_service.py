
from exceptions.bookings_exceptions import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from booking_table_wrapper.booking_table_wrapper import *

class BookingService:
    def __init__(self):
        try:
            self.booking_table_wrapper = BookingTableWrapper()
        except Exception as e:
            logger.error(e)

    def get_all_bookings(self):
        try:
            bookings = self.booking_table_wrapper.get_bookings()
            if len(bookings) == 0:
                raise BookingNotFoundException()
            else:
                return bookings
        except Exception as e:
            logger.error(e)
            return None


    def get_booking_by_id(self, booking_id: int = None):
        try:
            requested_booking = self.booking_table_wrapper.get_bookings(booking_id)
            if len(requested_booking) == 0:
                raise BookingNotFoundException(booking_id)
            else:
                return requested_booking
        except Exception as e:
            logger.error(e)
            raise e


