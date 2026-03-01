import customtkinter as ctk
from tkinter import messagebox


class CustomerManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", pady=10)

        self.customer_id_entry = ctk.CTkEntry(
            self.top_frame,
            placeholder_text="Enter Customer ID"
        )
        self.customer_id_entry.pack(pady=10)

        self.view_customer_btn = ctk.CTkButton(
            self.top_frame,
            text="View Customer Details",
            command=self.show_customer_details
        )
        self.view_customer_btn.pack(pady=5)

        self.view_bills_btn = ctk.CTkButton(
            self.top_frame,
            text="View Bills",
            command=self.show_bills
        )
        self.view_bills_btn.pack(pady=5)

        self.view_payments_btn = ctk.CTkButton(
            self.top_frame,
            text="View Payment History",
            command=self.show_payments
        )
        self.view_payments_btn.pack(pady=5)

        
        self.result_frame = ctk.CTkFrame(self)
        self.result_frame.pack(fill="both", expand=True, pady=10)

    def clear_results(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def show_customer_details(self):
        from services.customer_service import get_customer_details

        self.clear_results()

        try:
            customer_id = int(self.customer_id_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid Customer ID")
            return

        customer = get_customer_details(customer_id)

        if not customer:
            messagebox.showerror("Error", "Customer not found")
            return

        label = ctk.CTkLabel(
            self.result_frame,
            text=f"{customer['firstname']} {customer['lastname']}\n"
                 f"Address: {customer['address']}\n"
                 f"Phone: {customer['phone']}\n"
                 f"Type ID: {customer['type_id']}"
        )
        label.pack(pady=10)

    def show_bills(self):
        from services.bill_service import get_customer_bills

        self.clear_results()

        try:
            customer_id = int(self.customer_id_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid Customer ID")
            return

        bills = get_customer_bills(customer_id)

        if not bills:
            ctk.CTkLabel(self.result_frame, text="No bills found").pack(pady=10)
            return

        for bill in bills:
            ctk.CTkLabel(
                self.result_frame,
                text=f"Bill {bill['bill_id']} | "
                     f"{bill['month']}/{bill['year']} | "
                     f"Due: {bill['amount_due']} | "
                     f"Status: {bill['status']}"
            ).pack(pady=3)

    def show_payments(self):
        from services.payment_service import get_payment_history

        self.clear_results()

        try:
            customer_id = int(self.customer_id_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid Customer ID")
            return

        payments = get_payment_history(customer_id)

        if not payments:
            ctk.CTkLabel(self.result_frame, text="No payments found").pack(pady=10)
            return

        for p in payments:
            ctk.CTkLabel(
                self.result_frame,
                text=f"Payment {p[0]} | "
                     f"Bill {p[3]} | "
                     f"Amount: {p[1]} | "
                     f"Date: {p[2]}"
            ).pack(pady=3)
