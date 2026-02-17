from  datetime import date
from models.bill import Bill

class Payment:
    
    def __init__(self, paymentID: int, amountPaid: float, paymentMethods: str, bill: Bill):
        self.paymentID = paymentID
        self.paymentDate = date.today()
        self.amountPaid = amountPaid
        self.paymentMethods = paymentMethods
        self.bill = bill

    def processPayment(self):
        if self.amountPaid >= self.bill.amountDue:
            self.bill.updateBillStatus("Paid")
        else:
            self.bill.updateBillStatus("Partial")

    def getPaymentDetails(self):
            return f"Payment ID: {self.paymentID}, Amount Paid: {self.amountPaid}"
        