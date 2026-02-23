import tkinter as tk
from tkinter import messagebox
from services.payment_service import process_payment

class PaymentWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("Process Payment")
        self.window.geometry("350x200")

        tk.Label(window, text="Bill ID").pack()
        self.bill_entry = tk.Entry(window)
        self.bill_entry.pack()

        tk.Label(window, text="Amount").pack()
        self.amount_entry = tk.Entry(window)
        self.amount_entry.pack()

        tk.Button(window, text="Pay",
        command=self.pay).pack(pady=10)


    def pay(self):
        try:
            bill_id =int(self.bill_entry.get())
            amount = float(self.amount_entry.get())

            process_payment(bill_id, amount)

            messagebox.showinfo("Success", "Payment processed")

        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            