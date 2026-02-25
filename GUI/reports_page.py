import customtkinter as ctk
from services.bill_service import get_report_data


class ReportsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="System Reports", font=("Arial", 22, "bold"))
        title.pack(pady=20)

        data = get_report_data()

        total_revenue = data["total_revenue"]
        unpaid = data["unpaid_count"]
        paid = data["paid_count"]

        ctk.CTkLabel(self, text=f"Total Revenue: {total_revenue}").pack(pady=5)
        ctk.CTkLabel(self, text=f"Paid Bills: {paid}").pack(pady=5)
        ctk.CTkLabel(self, text=f"Unpaid Bills: {unpaid}").pack(pady=5)