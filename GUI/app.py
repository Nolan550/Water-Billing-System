import customtkinter as ctk
from GUI.login_window import LoginWindow

ctk.set_appearance_mode("light")      
ctk.set_default_color_theme("blue")   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Water Billing System")
        self.geometry("900x600")
        self.resizable(True, True)

        self.current_frame = None
        self.show_login()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginWindow(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_dashboard(self, user):
        from GUI.dashboard import Dashboard
        self.clear_frame()
        self.current_frame = Dashboard(self, user)
        self.current_frame.pack(fill="both", expand=True)