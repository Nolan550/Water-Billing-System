from datetime import date

class Meter:

    def __init__(self, meterID: int, previousReading: float, currentReading: float, readingDate: date):
        self.meterID = meterID
        self.previousReading = previousReading
        self.currentReading = currentReading
        self.readingDate = readingDate

    def recordReading(self, newReading: float, readingDate):
        self.previousReading = self.currentReading
        self.currentReading = newReading
        self.readingDate = date.today()

    def calculateConsumption(self):
        return self.currentReading - self.previousReading
    