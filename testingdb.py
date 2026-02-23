from services.payment_service import process_payment

result = process_payment(2, 2150)

if result:
    print("New Amount Paid:", result["new_amount_paid"])
    print("New Status:", result["status"])
else:
    print("Payment failed")