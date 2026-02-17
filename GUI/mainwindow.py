from datetime import date
from models.customer import Customer
from models.customerType import Customer_Type
from models.meter import Meter
from models.bill import Bill
from models.payment import Payment
import tkinter as tk
from tkinter import messagebox

class main_window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Billing Management System")
        self.root.geometry("500x400")

        self.title_label = tk.Label(self.root, text="Water billing System", font=("Arial", 16))
        self.title_label.pack(pady=10)

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

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()


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
        
        customer_Type = Customer_Type(1, "Residential", 2.5)

        previous_reading = 100
    
        meter = Meter(1, previous_reading, previous_reading, date.today())

        meter.record_reading(meter_reading, date.today())

        customer = Customer(1, name, "Nolan","Dar es Salaam", "0744097836", customer_Type, meter)

        bill = Bill(1, "March", 2026, customer)

        amount = bill.calculate_bill_amount()
        self.output_label.config(
            text=f"Consumption: {bill.water_consumption}\nAmount Due: {amount}"
        )


        ###
       # self.output_label.config(text=f"Bill generated for {name}")
    

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
