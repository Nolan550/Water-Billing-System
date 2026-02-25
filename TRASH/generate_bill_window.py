import tkinter as tk
from tkinter import messagebox
from services.bill_service import create_bill


class GenerateBillWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("Generate Bill")
        self.window.geometry("350x250")


        tk.Label(window, text="Customer ID").pack()
        self.customer_entry = tk.Entry(window)
        self.customer_entry.pack()

        tk.Label(window, text="Month").pack()
        self.month_entry = tk.Entry(window)
        self.month_entry.pack()

        tk.Label(window, text="Year").pack()
        self.year_entry = tk.Entry(window)
        self.year_entry.pack()

        tk.Button(window, text="Generate",
                  command=self.generate_bill).pack(pady=10)
        
    def generate_bill(self):
        try:
            customer_id = int(self.customer_entry.get())
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())

            bill_id = create_bill(customer_id, month, year)

            if bill_id:
                messagebox.showinfo("Success", f"Bill ID: {bill_id}")

            else:
                messagebox.showerror("Error", "Bill creation failed")

        except ValueError:
            messagebox.showerror("Error", "Invalid input")