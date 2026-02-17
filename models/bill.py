from models.customer import Customer

class Bill:

    def __init__ (self, bill_ID: int, billing_month: str, billing_year: int, customer: Customer):
        self.bill_ID = bill_ID
        self.billing_month = billing_month
        self.billing_year = billing_year
        self.bill_status = "Unpaid"
        self.water_consumption = 0.0
        self.amount_due = 0.0 
        self.customer = customer

    def calculate_bill_amount(self):
        self.water_consumption = self.customer.meter.calculate_consumption()
        rate = self.customer.customer_Type.get_rate_per_unit()
        self.amount_due = self.water_consumption * rate
        return self.amount_due
    
    def update_bill_status(self, status: str):
        self.bill_status = status

    def get_bill_details(self):
        return f"Bill ID: {self.bill_ID} \nAmount Due: {self.amount_due}\nStatus: {self.bill_status}"
    