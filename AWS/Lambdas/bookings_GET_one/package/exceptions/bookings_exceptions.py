class NoCarFoundException(Exception):
    def __init__(self, car_id: int):
        self.car_id = car_id
        self.message = f"Car with ID {car_id} not found"


class CarNotAvailableException(Exception):
    def __init__(self, car_id: int):
        self.car_id = car_id
        self.message = f"Car with ID {car_id} is not available"


class BookingOverlapException(Exception):
    def __init__(self, car_id: int):
        self.car_id = car_id
        self.message = "The car is already booked for the selected dates"


class BookingNotFoundException(Exception):
    def __init__(self, booking_id: int = None):
        self.booking_id = booking_id
        if self.booking_id is None:
            self.message = f"No bookings found"
        else:
            self.message = f"Booking with ID {booking_id} not found"


class BookingStateException(Exception):
    def __init__(self, status: str):
        self.message = f"Cannot update booking in {status} state"


class DateRangeException(Exception):
    def __init__(self):
        self.message = "End date must be after start date"


class BookingOverlapUpdateException(Exception):
    def __init__(self):
        self.message = "The requested dates overlap with another booking"


class PickupAfterReturnException(Exception):
    def __init__(self):
        self.message = "Return date must be after pickup date"


class FutureDateException(Exception):
    def __init__(self, date_type: str):
        self.message = f"{date_type} date cannot be in the future"


class ReturnWithoutPickupException(Exception):
    def __init__(self):
        self.message = "Cannot set return date without a pickup date"


class DateOutsideBookingPeriodException(Exception):
    def __init__(self, date_type: str):
        self.message = f"{date_type} date must be within the booking period"


class BookingStartDateException(Exception):
    def __init__(self):
        self.message = "Booking start date must be in the future, not today or in the past"

class ServiceUnavailableException(Exception):
    def __init__(self, service_name: str):
        self.message = "Service {} is unavailable".format(service_name)

class InvalidBookingIdException(Exception):
    def __init__(self, booking_id):
        self.message = "Invalid booking ID: {}".format(booking_id)