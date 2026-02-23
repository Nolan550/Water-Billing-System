import tkinter as tk
from GUI.generate_bill_window import GenerateBillWindow
from GUI.payment_window import PaymentWindow
from GUI.view_bills_window import ViewBillsWindow

class Dashboard:
    def __init__(self, window, login_root, user):
        self.window = window
        self.login_root = login_root
        self.user = user

        self.window.title("Dashboard")
        self.window.geometry("400x300")

        tk.Label(self.window, text=f"Welcome (Role: {user['role']})",
                 font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.window, text="Generate Bill",
                  command=self.open_generate_bill).pack(pady=5)
        
        tk.Button(self.window, text="Process Payment",
                  command=self.open_payment).pack(pady=5)
        
        tk.Button(self.window, text="View Customer Bills",
                  command=self.open_view_bills).pack(pady=5)
        
        tk.Button(self.window, text="Logout",
                  command=self.logout).pack(pady=10)
        

    def open_generate_bill(self):
        window =tk.Toplevel(self.window)
        GenerateBillWindow(window)

    def open_payment(self):
        window = tk.Toplevel(self.window)
        PaymentWindow(window)

    def open_view_bills(self):
        window = tk.Toplevel(self.window)
        ViewBillsWindow(window)

    def Logout(self):
        self.window.destroy()
        self.login_root.deiconfiy()