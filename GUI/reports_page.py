import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.report_service import get_usage_by_sector


class ReportsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Water Usage Analytics", font=("Arial", 22, "bold"))
        title.pack(pady=20)

        self.show_chart()

    def show_chart(self):
        data = get_usage_by_sector()

        if not data:
            return

        sectors = [row[0] for row in data]
        usage = [float(row[1] or 0) for row in data]

        fig, ax = plt.subplots()
        ax.bar(sectors, usage)
        ax.set_title("Water Usage by Sector")
        ax.set_ylabel("Units Used")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()