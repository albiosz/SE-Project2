from datetime import date

def calculate_booking_duration(start_date: date, end_date: date):
    """Calculate booking duration in days"""
    return (end_date - start_date).days + 1

