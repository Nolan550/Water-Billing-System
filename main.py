from datetime import date
from models.customerType import CustomerType
from models.meter import Meter
from models.customer import Customer
from models.bill import Bill
from models.payment import Payment

residential = CustomerType(1, "Residential", 2.5)

meter = Meter(101, 100, 150, date.today())

customer = Customer("C001", "John", " Doe", "Main Street", 1234567, residential, meter)

bill = Bill(1, "March", 2026, "Unpaid", customer)
bill.calculateBillAmount()


payment = Payment(1, 125, "Cash", bill)
payment.processPayment()


#print(bill.getBillDetails())

print(payment.getPaymentDetails())