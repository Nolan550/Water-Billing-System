from models.customer import Customer

class Bill:

    def __init__ (self, billID: int, billingMonth: str, billingYear: int, billStatus: str, customer: Customer):
        self.billID = billID
        self.billingMonth = billingMonth
        self.billingYear = billingYear
        self.billStatus = billStatus
        self.customer = customer

    def calculateBillAmount(self):
        self.waterConsumption = self.customer.meter.calculateConsumption()
        rate = self.customer.customerType.getRatePerUnit()
        self.amountDue = self.waterConsumption * rate
        return self.amountDue
    
    def updateBillStatus(self, status: str):
        self.billStatus = status

    def getBillDetails(self):
        return f"Bill ID: {self.billID} \nAmount Due: {self.amountDue}\nStatus: {self.billStatus}"
    