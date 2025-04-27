
from exceptions.cars_exceptions import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from car_table_wrapper.car_table_wrapper import *

class CarService:
    def __init__(self):
        try:
            self.car_table_wrapper = CarTableWrapper()
        except Exception as e:
            logger.error(e)

    def get_all_cars(self):
        try:
            items = self.car_table_wrapper.get_all_cars()
            if len(items) == 0:
                raise CarNotFoundException()
            else:
                return items
        except Exception as e:
            logger.error(e)
            return None


    def get_car_by_id(self, car_id: int = None):
        try:
            requested_items = self.car_table_wrapper.get_car(car_id)
            if len(requested_items) == 0:
                raise CarNotFoundException(car_id)
            elif len(requested_items) == 1:
                return requested_items[0]
            else:
                raise TooManyCarsException(car_id)
        except Exception as e:
            logger.error(e)
            raise e


