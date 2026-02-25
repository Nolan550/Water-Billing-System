import customtkinter as ctk
from tkinter import messagebox
from services.customer_service import create_customer


class CustomersPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Add Customer", font=("Arial", 22, "bold"))
        title.pack(pady=20)

        self.firstname_entry = ctk.CTkEntry(self, placeholder_text="First Name")
        self.firstname_entry.pack(pady=5)

        self.lastname_entry = ctk.CTkEntry(self, placeholder_text="Last Name")
        self.lastname_entry.pack(pady=5)

        self.address_entry = ctk.CTkEntry(self, placeholder_text="Address")
        self.address_entry.pack(pady=5)

        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Phone")
        self.phone_entry.pack(pady=5)

        self.type_entry = ctk.CTkEntry(self, placeholder_text="Type ID (1,2,3)")
        self.type_entry.pack(pady=5)

        self.add_btn = ctk.CTkButton(self, text="Add Customer", command=self.add_customer)
        self.add_btn.pack(pady=10)

    def add_customer(self):
        try:
            create_customer(
                self.firstname_entry.get(),
                self.lastname_entry.get(),
                self.address_entry.get(),
                self.phone_entry.get(),
                int(self.type_entry.get())
            )

            messagebox.showinfo("Success", "Customer added successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))