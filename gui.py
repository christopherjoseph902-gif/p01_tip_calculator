import customtkinter as ctk #noqa
#import  the GUI library                           #CTkFrame: a container that holds other widgets
                                                   #CTkLable: Display text

class TipCalculatorApp(ctk.CTk):
    #DEFINE OUR APPLICATION WINDOW
    """"A class to initialize the application Window"""
    def __init__(self) ->None: #initialize the application window
        super().__init__()  #Initialize the parent CTk window
        self.title("Tip Calculator") # set the windows title
        self.geometry("1100*700") #The actual size of the  window
        self.minsize(900,600) #The min size of window to prevent it from being too small

        ctk.set_appearance_mode("dark") # enable dark appearance 
        ctk.set_default_color_theme("blue") #select the blue accent theme 

        #CONFIGURING WINDOWS LAY OUT

        self.grid_columnconfigure(1,weight =1)
        self.grid_rowconfigure( 0,weight =1 )

        #side bar
        self.sidebar = ctk.CTkFrame(
            self,
            width =200,
            corner_radius=0
        )
        self.sidebar.grid( #Position widget in a row and column
            row=0,
            column=0,
            sticky="nsew"
        )
        self.sidebar.grid_propagate(False)

        #Side title
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="TIP CALCULATOR",
            font=("Arial", 20, "bold")
        )

        self.logo.pack(pady=30) # arrange widgets inside a container


        #Main content area
        self.main_area = ctk.CTkFrame(
            self,
            corner_radius=0
         )
        self.main_area.grid(
            row=0,
            column=1,
            sticky="nsew",# a Widget stretch in all four direction
            padx=15,
            pady=15
        )
        #Dashboard heading
        self.heading =  ctk.CTkLabel(
            self.main_area,
            text = "Dash board",
            font=("Arial", 28, "bold")
        )
        self.heading.pack(anchor="w", padx=25, pady=25) # arrange widget in a  container


if __name__ == "__main__":
    app = TipCalculatorApp()
    app.mainloop() #Start the GUI event loop and wait for user interaction

