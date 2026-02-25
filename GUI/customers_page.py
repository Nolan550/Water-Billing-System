import customtkinter as ctk


class CustomersPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Customers",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=20)

        ctk.CTkLabel(self, text="Add or manage customers here").pack()