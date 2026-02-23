import tkinter as tk
from tkinter import messagebox
from services.auth_service import login_user
from GUI.dashboard import Dashboard

class LoginWindow:

    def __init__(self,root):
        self.root = root

        tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Username").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()


        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password= self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return
        
        user = login_user(username, password)

        if user:
            messagebox.showinfo("Success", "Login successful")

            self.root.withdraw() 

            dashboard_window = tk.Toplevel(self.root)
            Dashboard(dashboard_window, self.root, user)

        else:
            messagebox.showerror("Error", "Invalid credentials")