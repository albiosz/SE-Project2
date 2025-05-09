

import boto3
import botocore
from boto3.dynamodb.conditions import Key

from service.constants import SERVICE_NAME, RESOURCE_NAME, TABLE_NAME
# from package.service.constants import SERVICE_NAME, RESOURCE_NAME, BOOKINGS_DB_ENDPOINT, TABLE_NAME       # local testing

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from package.exceptions.bookings_exceptions import ServiceUnavailableException

class BookingTableWrapper:
    def __init__(self):
        try:
            self.table = boto3.resource(RESOURCE_NAME).Table(TABLE_NAME)
            # only for local testing
            # self.table = boto3.resource(RESOURCE_NAME, endpoint_url = "http://localhost:8000").Table(TABLE_NAME)
            print("Table created successfully")
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

        if booking_id is None:
            return self.table.scan().get("Items")
        else:
            return self.table.query(IndexName="get_booking_efficiently",
                                    KeyConditionExpression=Key("id").eq(booking_id)).get("Items")    # don't need consistent reads


