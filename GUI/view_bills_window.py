import tkinter as tk
from services.bill_service import get_customer_bills

class ViewBillsWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("View Bills")
        self.window.geometry("500x300")


        tk.Label(window, text="Customer ID").pack()
        self.customer_entry = tk.Entry(window)
        self.customer_entry.pack()

        tk.Button(window, text="Load Bills",
                  command=self.load_bills).pack(pady=5)
        
        self.output =tk.Text(window, height=10, width=60)
        self.output.pack()

    def load_bills(self):
        self.output.delete("1.0", tk.END)
        try:
            customer_id = int(self.customer_entry.get())
            bills = get_customer_bills(customer_id)

            for bill in bills:
                self.output.insert(tk.END,
                           f"Bill ID: {bill['bill_id']} | "
                           f"Amount: {bill['amount_due']} | "
                           f"Status: {bill['status']}\n"
                           )
                
        except ValueError:
            self.output.insert(tk.END, "Invalid Customer ID")
        
    