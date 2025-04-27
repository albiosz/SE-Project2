

from fastapi import HTTPException, status
from package.exceptions.bookings_exceptions import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from package.booking_table_wrapper.booking_table_wrapper import BookingTableWrapper
from package.exceptions.bookings_exceptions import ServiceUnavailableException


def get_all_bookings():
    try:
        requested_booking = BookingTableWrapper.get_bookings()
        if len(requested_booking) == 0:
            raise BookingNotFoundException()
        else:
            return requested_booking
    except Exception as e:
        logger.error(e)
        return None


def get_booking_by_id(booking_id: int):
    try:
        requested_booking = BookingTableWrapper.get_bookings(booking_id)
        if len(requested_booking) == 0:
            raise BookingNotFoundException(booking_id)
        else:
            return requested_booking
    except Exception as e:
        logger.error(e)
        raise e
