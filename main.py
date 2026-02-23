import tkinter as tk

from GUI.login_window import LoginWindow

def main():
    root =tk.Tk()
    root.title("Water Billing System")
    root.geometry("700x650")
    LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()