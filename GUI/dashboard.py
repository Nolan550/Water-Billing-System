import customtkinter as ctk

from GUI.customer_managment_page import CustomerManagementPage


class Dashboard(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)

        self.master = master
        self.user = user

        self.pack(fill="both", expand=True)

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.sidebar_label = ctk.CTkLabel(
            self.sidebar,
            text="Dashboard",
            font=("Arial", 20, "bold")
        )
        self.sidebar_label.pack(pady=20)

        
        if self.user["role"] in ["admin", "staff"]:

            self.billing_btn = ctk.CTkButton(
            self.sidebar,
            text="Billing",
            command=self.open_billing
            )
            self.billing_btn.pack(pady=10, fill="x", padx=20)


        if self.user["role"] in ["admin", "staff"]:
            self.payments_btn = ctk.CTkButton(
            self.sidebar,
            text="Payments",
            command=self.open_payments
            )
            self.payments_btn.pack(pady=10, fill="x", padx=20)
            


        if self.user["role"] == "admin":
            self.reports_btn = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            command=self.open_reports
            
        )
            self.reports_btn.pack(pady=10, fill="x", padx=20)
            
            self.customers_btn = ctk.CTkButton(
            self.sidebar,
            text="Add Customer",
            command=self.open_customers
            )
            self.customers_btn.pack(pady=10, fill="x", padx=20) 
            
           
            

            self.manage_customer_btn = ctk.CTkButton(
            self.sidebar,
            text="Manage Customer",
            command=self.open_customer_management
            )
            self.manage_customer_btn.pack(pady=10)

        
        self.logout_btn = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            fg_color="red",
            command=self.logout
            )
        self.logout_btn.pack(side="bottom", pady=20, fill="x", padx=20)
        
        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.show_welcome()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_content()
        label = ctk.CTkLabel(
            self.content,
            text=f"Welcome {self.user['username']}",
            font=("Arial", 24, "bold")
        )
        label.pack(pady=50)

    def open_billing(self):
        from GUI.billing_page import BillingPage
        self.clear_content()
        BillingPage(self.content).pack(fill="both", expand=True)

    def open_payments(self):
        from GUI.payments_page import PaymentsPage
        self.clear_content()
        PaymentsPage(self.content).pack(fill="both", expand=True)

    def open_reports(self):
        from GUI.reports_page import ReportsPage
        self.clear_content()
        ReportsPage(self.content).pack(fill="both", expand=True)
    def show_bills(self):
        from services.bill_service import get_customer_bills

        customer_id = int(self.customer_id_entry.get())
        bills = get_customer_bills(customer_id)

        self.clear_content()

        for bill in bills:
            label = ctk.CTkLabel(
            self,
            text=f"Bill {bill['bill_id']} | {bill['month']}/{bill['year']} | "
                 f"Consumption: {bill['consumption']} | "
                 f"Amount Due: {bill['amount_due']} | "
                 f"Status: {bill['status']}"
            )
            label.pack(pady=5)
    
    
    def open_customers(self):
        from GUI.customers_page import CustomersPage
        self.clear_content()
        CustomersPage(self.content).pack(fill="both", expand=True)

    def logout(self):
        self.destroy()              # Destroy dashboard completely
        self.master.show_login()
        
    def open_customer_management(self):
        from GUI.customer_managment_page import CustomerManagementPage
        self.clear_content()
        CustomerManagementPage(self.content)
    

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

