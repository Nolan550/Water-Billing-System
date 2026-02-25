import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(pady=20)

        cards_frame = ctk.CTkFrame(self)
        cards_frame.pack(pady=20)

        for text, value in [
            ("Total Customers", "1,379"),
            ("Monthly Revenue", "17,100 TZS"),
            ("Water Usage", "5,700 m³"),
            ("Collection Rate", "94.2%")
        ]:
            card = ctk.CTkFrame(cards_frame, width=200, height=120)
            card.pack(side="left", padx=15)
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=text).pack(pady=10)
            ctk.CTkLabel(
                card,
                text=value,
                font=ctk.CTkFont(size=20, weight="bold")
            ).pack()