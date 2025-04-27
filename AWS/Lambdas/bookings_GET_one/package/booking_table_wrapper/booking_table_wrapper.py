

import boto3
import botocore
from boto3.dynamodb.conditions import Key

from service.constants import SERVICE_NAME, RESOURCE_NAME, TABLE_NAME

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from exceptions.bookings_exceptions import ServiceUnavailableException

class BookingTableWrapper:
    def __init__(self):
        try:
            # only when run locally
            # self.table = boto3.resource(RESOURCE_NAME, endpoint_url = "http://localhost:8000").Table(TABLE_NAME)
            self.table = boto3.resource(RESOURCE_NAME).Table(TABLE_NAME)
            print("Table created successfully")
        except botocore.exceptions.ClientError as err:
            logger.error(
                "Table %s is unavailable. %s: %s",
                TABLE_NAME,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"])
            raise ServiceUnavailableException(SERVICE_NAME)


# returns a list of results for conform results
    def get_booking(self, booking_id: int = None):
        if self.table is None:
            raise ServiceUnavailableException(TABLE_NAME)
        return self.table.query(IndexName="id-index",
                                KeyConditionExpression=Key("id").eq(booking_id)).get("Items")    # don't need consistent reads

    def get_all_bookings(self):
        return self.table.scan().get("Items")