import customtkinter as ctk
from tkinter import messagebox
from services.payment_service import process_payment


class PaymentsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Process Payment", font=("Arial", 22, "bold"))
        title.pack(pady=20)

        self.bill_id_entry = ctk.CTkEntry(self, placeholder_text="Bill ID", width=300)
        self.bill_id_entry.pack(pady=10)

        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount Paid", width=300)
        self.amount_entry.pack(pady=10)

        self.pay_button = ctk.CTkButton(self, text="Submit Payment", command=self.pay)
        self.pay_button.pack(pady=20)

    def pay(self):
        try:
            bill_id = int(self.bill_id_entry.get())
            amount = float(self.amount_entry.get())

            process_payment(bill_id, amount)

            messagebox.showinfo("Success", "Payment processed successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))