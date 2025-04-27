

import boto3
import botocore

from package.service.constants import SERVICE_NAME, RESOURCE_NAME, TABLE_NAME

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from AWS.Lambdas.bookings_GET_all.package.exceptions.bookings_exceptions import ServiceUnavailableException

class BookingTableWrapper:
    def __init__(self):
        try:
            self.table = boto3.resource(RESOURCE_NAME).Table(TABLE_NAME)
        except botocore.exceptions.ClientError as err:
            logger.error(
                "Table %s is unavailable. %s: %s",
                TABLE_NAME,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"])
            raise ServiceUnavailableException(SERVICE_NAME)


# returns a list of results for conform results
    def get_bookings(self, booking_id: int = None):
        if self.table is None:
            raise ServiceUnavailableException(TABLE_NAME)

        query_result = []
        if booking_id is None:
            return query_result.append(self.table.scan())
        else:
            return query_result.extend(self.table.get_item(Key={"id": booking_id}))     # don't need consistent reads