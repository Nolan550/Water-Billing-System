from datetime import date
from models.customer import Customer
from models.customerType import Customer_Type
from models.meter import Meter
from models.bill import Bill
from models.payment import Payment
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class main_window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Billing Management System")
        self.root.geometry("500x400")

        self.title_label = tk.Label(self.root, text="Water billing System", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.customer_type_label = tk.Label(self.root, text="Customer Type:")
        self.customer_type_label.pack()

        self.customer_type_var = tk.StringVar()
        self.type_dropdown = ttk.Combobox(self.root, textvariable=self.customer_type_var, state="readonly")

        self.type_dropdown["values"] = ("Residential", "Commercial", "Industrial")
        self.type_dropdown.current(0)
        self.type_dropdown.pack()

        self.name_entry = tk.Entry(self.root, text="Customer First Name:")
        self.name_entry.pack()

        self.name_entry = tk.Entry(self.root, text="Customer Last Name:")
        self.name_entry.pack()

        self.meter_label = tk.Label(self.root, text="Current Meter Reading:")
        self.meter_label.pack()

        self.meter_entry = tk.Entry(self.root)
        self.meter_entry.pack()

        self.generate_bill_button = tk.Button(self.root, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.pack(pady=10)

        self.output_label = tk.Label(self.root, height=15, width=60)
        self.output_label.pack(pady=10)


    def generate_bill(self):
        name = self.name_entry.get()
        meter_reading = self.meter_entry.get()

        if name == "" or meter_reading == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            meter_reading = float(meter_reading)
        except ValueError:
            messagebox.showerror("Error", "Meter reading must be a number!")
            return
        
        selected_type = self.customer_type_var.get()

        if selected_type == "Residential":
            rate = 2.5
        elif selected_type == "Commercial":
            rate = 4.0
        else:
            rate = 6.0

        customer_Type = Customer_Type(1, selected_type, rate)

        previous_reading = 100
    
        meter = Meter(1, previous_reading, previous_reading, date.today())

        meter.record_reading(meter_reading, date.today())

        customer = Customer(1, name, "Nolan","Dar es Salaam", "0744097836", customer_Type, meter)

        bill = Bill(1, "March", 2026, customer)

        amount = bill.calculate_bill_amount()
        amount_due = amount

        details =f"""
        ---------------WATER BILL DETAILS----------------
        Customer Name: {customer.cus_Fname} {customer.cus_Lname}
        Customr Type: {selected_type}

        Previous Meter Reading: {previous_reading}
        Current Meter Reading: {meter.current_reading}
        Water Consumption: {meter.calculate_consumption()} units

        Rate Per Unit: {rate} TZS
        Amount Due: {bill.amount_due} TZS

        Status: {bill.bill_status}
        Billing Period: {bill.billing_month} {bill.billing_year}
        ------------------------------------------------
        """
        print(details)
        

    def run(self):
        self.root.mainloop()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Water Billing Managment System",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)

        add_customer_button = tk.Button(
            self.root,
            text = "Add Customer",
            width = 20
        )
        add_customer_button.pack(pady=10)

        generate_bill_button = tk.Button(
            self.root,
            text="Generate Bill",
            width = 20
        )
        generate_bill_button.pack(pady = 10)

        payment_button = tk.Button(
            self.root,
            text="Process Payment",
            width = 20
        )
        payment_button.pack(pady=10)

        view_bills_button =  tk.Button(
            self.root,
            text="View Bills",
            width = 20
        )
        view_bills_button.pack(pady=10)

    def run(self):
        self.root.mainloop()
