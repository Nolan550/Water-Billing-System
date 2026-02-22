from datetime import date
from models.customer import Customer
from models.customerType import Customer_Type
from models.meter import Meter
from models.bill import Bill
from models.payment import Payment
from services.customer_service import add_customer
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class main_window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Billing Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#EAF6FF")

        self.header = tk.Label(self.root, text=" 💧 WATER BILLING MANAGEMENT SYSTEM", font=("Helvetica", 18, "bold"), bg="#0A3D62", fg="white", pady=15)
        self.header.pack(fill="x")

        self.main_frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        self.main_frame.pack(pady=20, padx=40)

        self.form_frame = tk.Frame(self.main_frame, bg="white")
        self.form_frame.pack(pady=20)

        tk.Label(self.form_frame, text="Customer Type:", bg="white", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)


        self.customer_type_var = tk.StringVar()
        self.type_dropdown = ttk.Combobox(
            self.form_frame,
            textvariable=self.customer_type_var,
            state="readonly",
            width=25
        )
        self.type_dropdown["values"] = ("Residential", "Commercial", "Industrial")
        self.type_dropdown.current(0)
        self.type_dropdown.grid(row=0, column=1, pady=10)

        
        tk.Label(self.form_frame, text="Customer First Name:", bg="white", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
        

        self.name_entry = tk.Entry(self.form_frame, width=28)
        self.name_entry.grid(row=1, column=1, pady=5)

        
        tk.Label(self.form_frame, text="Customer Last Name:", bg="white", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
        

        self.lname_entry = tk.Entry(self.form_frame, width=28)
        self.lname_entry.grid(row=2, column=1, pady=5)

        
        tk.Label(self.form_frame, text="Current Meter Reading:", bg="white", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=5)
        

        self.meter_entry = tk.Entry(self.form_frame, width=28)
        self.meter_entry.grid(row=3, column=1, pady=5)

        
        self.generate_bill_button = tk.Button(
            self.main_frame,
            text="Generate Bill",
            bg="#1E90FF",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            activebackground="#0A3D62",
            relief="flat",
            command=self.generate_bill
        )
        self.generate_bill_button.pack(pady=15)

        
        self.output_label = tk.Label(
            self.root,
            bg="#F4FAFF",
            fg="#0A3D62",
            font=("Courier", 10),
            height=15,
            bd=1,
            relief="solid",
            padx=10,
            pady=10,
            width=80,
            justify="left",
            anchor="nw"
        )
        self.output_label.pack(pady=10)

    

    def generate_bill(self):

        name = self.name_entry.get()
        lname = self.lname_entry.get()
        meter_reading = self.meter_entry.get()

        if name == "" or lname == "" or meter_reading == "":
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            meter_reading = float(meter_reading)
        except ValueError:
            messagebox.showerror("Error", "Meter reading must be a number!")
            return

        selected_type = self.customer_type_var.get()


        customer_type = get_customer_type_by_name(selected_type)
        type_id = customer_type["type_id"]
        rate = customer = customer_type["rate_per_unit"]


        customer_id = add_customer(
            name,
            lname,
            "Dar es Salaam",
            "0744097836",
            type_id
        )
        

        previous_reading = 100
        consumption = meter_reading - previous_reading

        add_meter_reading(customer_id, previous_reading, meter_reading)

        amount_due = consumption * rate

        create_bill(
            customer_id,
            "March",
            2026,
            consumption
            amount_due
        )

        

        details = f"""
--------------- WATER BILL DETAILS ----------------

Customer Name: {customer.cus_Fname} {customer.cus_Lname}
Customer Type: {selected_type}

Previous Meter Reading: {previous_reading}
Current Meter Reading: {meter.current_reading}
Water Consumption: {meter.calculate_consumption()} units

Rate Per Unit: {rate} TZS
Amount Due: {bill.amount_due} TZS

Status: {bill.bill_status}
Billing Period: {bill.billing_month} {bill.billing_year}

---------------------------------------------------
"""

        
        self.output_label.config(text=details)


    

    def run(self):
        self.root.mainloop()