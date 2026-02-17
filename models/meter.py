from datetime import date

class Meter:

    def __init__(self, meter_ID: int, previous_reading: float, current_reading: float, reading_date: date):
        self.meter_ID = meter_ID
        self.previous_reading = previous_reading
        self.current_reading = current_reading
        self.reading_date = reading_date

    def record_reading(self, new_reading: float, reading_date: date):
        self.previous_reading = self.current_reading
        self.current_reading = new_reading
        self.reading_date = reading_date

    def calculate_consumption(self):
        return self.current_reading - self.previous_reading
    