from typing import List
from models.meter import Meter
from models.customerType import Customer_Type

class Customer:

    def __init__ (self, customer_ID, cus_Fname, cus_Lname, address, phone_number, customer_Type: Customer_Type, meter: Meter):
        self.customer_ID = customer_ID
        self.cus_Fname = cus_Fname
        self.cus_Lname = cus_Lname
        self.address = address
        self.phone_number = phone_number
        self.customer_Type = customer_Type
        self.meter = meter
        self.bills: List = []

    def get_customer_details(self):
        return f"Customer ID: {self.customer_ID}\nName: {self.cus_Fname} {self.cus_Lname}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nCustomer Type: {self.customer_Type.type_name}\nMeter ID: {self.meter.meter_ID}"
    
    def view_bills(self):
        return self.bills
    

