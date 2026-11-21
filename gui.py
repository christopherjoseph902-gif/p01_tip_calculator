import customtkinter as ctk


class TipCalculatorApp(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()# Initializes the window

        self.title("Tip Calculator")#The title of the  calcualtor
        self.geometry("1100x700")#defines the dimension of the  screen
        self.minsize(900, 600)# initializes the minimum size of the computer screen

        #Appearance settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configure the main window layout
        self.grid_columnconfigure(1,weight = 1 )# allow  column   to expand while windows grow
        self.grid_rowconfigure(0, weight = 1)# alow row zero to expand vertically

        #sidebar
        self.sidebar = ctk.CTkFrame(  #create a container
            self,
            width = 200,#The  width
            corner_radius = 0
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"#stretches it in four direction
        )

        self.sidebar.propagate(False)#Prevent the child widget from changing the parent size automatically

        self.logo =ctk.CTkLabel(#used to display text
            self.sidebar,#make the label a child of the side bar
            text = "TIP CALCULATOR",
            font = ("Arial", 20, "bold")#sets the typography
        )
        self.logo.pack(pady=30)#positions it with vertical spacing

        self.dashboard_button = 

if __name__ == "__main__":
    app = TipCalculatorApp()
    app.mainloop()#Start GUI main loop