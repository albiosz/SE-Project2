

from fastapi import HTTPException, status
from package.exceptions.bookings_exceptions import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from AWS.Lambdas.bookings_GET_all.package.booking_table_wrapper.booking_table_wrapper import BookingTableWrapper
from AWS.Lambdas.bookings_GET_all.package.exceptions.bookings_exceptions import ServiceUnavailableException


def get_all_bookings():
    try:
        return BookingTableWrapper.get_bookings()
    except Exception as e:
        logger.error(e)
        return None