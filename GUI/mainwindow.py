import tkinter as tk
from tkinter import messagebox

class main_window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Billing Management System")
        self.root.geometry("500x400")

        self.title_label = tk.Label(self.root, text="Water billing System", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.name_entry = tk.Entry(self.root, text="Customer Name:")
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
            messagebox.showerror("Error", "All field are required!")
            return
        self.output_label.config(text=f"Bill generated for {name}")
    

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
