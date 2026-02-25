import customtkinter as ctk
from tkinter import ttk, messagebox
from .generate_bill_window.GenerateBillWindow import generate_bill


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
        try:
            customer_id = int(self.customer_id_entry.get())
            reading = float(self.meter_reading_entry.get())
            month = self.month_entry.get()

            generate_bill(customer_id, reading, month)

            messagebox.showinfo("Success", "Bill generated")

        except Exception as e:
            messagebox.showerror("Error", str(e))