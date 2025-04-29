class CarNotFoundException(Exception):
    def __init__(self, car_id: int):
        self.car_id = car_id
        self.message = f"Car with ID {car_id} not found"
        super().__init__(self.message)

class InvalidCarIdException(Exception):
    def __init__(self, car_id: int):
        self.message = "Invalid car ID: {}".format(car_id)

class TooManyResultsException(Exception):
    def __init__(self, car_id: int = None):
        self.message = "Too many results for car ID: {}".format(car_id)

class ServiceUnavailableException(Exception):
    def __init__(self, service_name: str):
        self.message = "Service {} is unavailable".format(service_name)