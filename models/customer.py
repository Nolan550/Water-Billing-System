from typing import List
from models.meter import Meter
from models.customerType import CustomerType

class Customer:

    def __init__ (self, customerID, cusFname, cusLname, address, phoneNumber, customerType: CustomerType, meter: Meter):
        self.customerID = customerID
        self.cusFname = cusFname
        self.cusLname = cusLname
        self.address = address
        self.phoneNumber = phoneNumber
        self.customerType = customerType
        self.meter = meter
        self.bills: List = []

    def getCustomerDetails(self):
        return f"Customer ID: {self.customerID}\nName: {self.cusFname} {self.cusLname}\nAddress: {self.address}\nPhone Number: {self.phoneNumber}\nCustomer Type: {self.customerType.typeName}\nMeter ID: {self.meter.meterID}"
    
    def viewBills(self):
        return self.bills
    

