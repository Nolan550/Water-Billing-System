import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import login_user


class LoginWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.configure(fg_color="white")

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Water Billing System",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=40)

        # Card Frame
        self.card = ctk.CTkFrame(self, width=400, height=350, corner_radius=15)
        self.card.pack()
        self.card.pack_propagate(False)

        self.login_label = ctk.CTkLabel(
            self.card,
            text="Login",
            font=("Arial", 22, "bold")
        )
        self.login_label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Username",
            width=300
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Password",
            show="*",
            width=300
        )
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self.card,
            text="Login",
            width=300,
            command=self.login
        )
        self.login_button.pack(pady=15)

        self.register_button = ctk.CTkButton(
            self.card,
            text="Register",
            width=300,
            fg_color="gray",
            command=self.open_register
        )
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = login_user(username, password)

        if user:
            self.master.show_dashboard(user)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def open_register(self):
        from GUI.register_window import RegisterWindow
        self.master.clear_frame()
        self.master.current_frame = RegisterWindow(self.master)
        self.master.current_frame.pack(fill="both", expand=True)