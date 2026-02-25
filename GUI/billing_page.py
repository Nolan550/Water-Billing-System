import customtkinter as ctk
from tkinter import ttk, messagebox
from services.bill_service import create_bill


class BillingPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Generate Bill", font=("Arial", 22, "bold"))
        title.pack(pady=20)

        self.customer_id_entry = ctk.CTkEntry(self, placeholder_text="Customer ID")
        self.customer_id_entry.pack(pady=5)

        self.meter_reading_entry = ctk.CTkEntry(self, placeholder_text="Meter Reading")
        self.meter_reading_entry.pack(pady=5)

        self.month_entry = ctk.CTkEntry(self, placeholder_text="Month (e.g. 2026-02)")
        self.month_entry.pack(pady=5)

        self.generate_btn = ctk.CTkButton(self, text="Generate Bill", command=self.generate)
        self.generate_btn.pack(pady=10)

    def generate(self):
        def generate(self):
            try:
                customer_id = int(self.customer_id_entry.get())
                month_year = self.month_entry.get()  # e.g 2026-02

                year, month = month_year.split("-")
                year = int(year)
                month = int(month)

                bill_id = create_bill(customer_id, month, year)

                if bill_id:
                    messagebox.showinfo("Success", f"Bill ID: {bill_id}")
                else:
                    messagebox.showerror("Error", "Bill creation failed")

            except Exception as e:
                messagebox.showerror("Error", str(e))