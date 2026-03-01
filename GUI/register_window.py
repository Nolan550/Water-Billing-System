import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import register_user


class RegisterWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.title_label = ctk.CTkLabel(
            self,
            text="Register New User",
            font=("Arial", 26, "bold")
        )
        self.title_label.pack(pady=40)

        self.card = ctk.CTkFrame(self, width=400, height=450, corner_radius=15)
        self.card.pack()
        self.card.pack_propagate(False)

        self.username_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Username",
            width=300
        )
        self.username_entry.pack(pady=15)

        self.password_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Password",
            show="*",
            width=300
        )
        self.password_entry.pack(pady=15)

        
        self.role_option = ctk.CTkOptionMenu(
            self.card,
            values=["admin", "staff"],
            width=300
        )
        self.role_option.set("staff")
        self.role_option.pack(pady=15)

        self.register_button = ctk.CTkButton(
            self.card,
            text="Register",
            width=300,
            command=self.register
        )
        self.register_button.pack(pady=20)

        self.back_button = ctk.CTkButton(
            self.card,
            text="Back to Login",
            width=300,
            fg_color="gray",
            command=self.back_to_login
        )
        self.back_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_option.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        success = register_user(username, password, role)

        if success:
            messagebox.showinfo("Success", "User registered successfully")
            self.back_to_login()
        else:
            messagebox.showerror("Error", "Registration failed")

    def back_to_login(self):
        self.master.show_login()
