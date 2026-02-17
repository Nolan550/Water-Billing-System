from  datetime import date
from models.bill import Bill

class Payment:
    
    def __init__(self, payment_ID: int, amount_paid: float, payment_methods: str, bill: Bill):
        self.payment_ID = payment_ID
        self.payment_date = date.today()
        self.amount_paid = amount_paid
        self.payment_methods = payment_methods
        self.bill = bill

    def process_payment(self):
        if self.amount_paid >= self.bill.amount_due:
            self.bill.update_bill_status("Paid")
        else:
            self.bill.update_bill_status("Partial")
            

    def get_payment_details(self):
        if self.amount_paid < self.bill.amount_due:
            print(f"Remaining Debt: { self.bill.amount_due - self.amount_paid}")
        return f"Payment ID: {self.payment_ID}\nAmount Paid: {self.amount_paid}"
    

        