from cgi import print_arguments
from msilib import Dialog
import tkinter
import datetime
from tkinter import messagebox
from tkinter.filedialog import Open, SaveAs, SaveFileDialog
from tkinter.tix import PopupMenu
from typing import Self
from winreg import SaveKey


class MainWindow(object):

    

    def __init__(self,window):
        self.window =window
    def popUp(window,title,message): 
        
        return messagebox.show_info(title,message)
 
          
    def bB(): return True
    def mA(): return True
    Modes=["Auto", "Manual", "Signal","None"]
    
    def mode ():
    
        return
    def AutoTrading():
        
        return
    
    def show():
        window = tkinter.Tk()
        window.iconbitmap('./UI/images/blueyes.ico')
        
        
        menuBar = tkinter.Menu(window)
        window.config(menu=menuBar,borderwidth=20,border=12 )       
        dashboard = tkinter.Canvas(window,border=158,background='black',closeenough=80)
        dashboard.pack()
        
        autoTrading = tkinter.Button(window, text="Auto Trading", pady=10, command=lambda :tkinter.Label("Auto Trading"))
        autoTrading.pack()
    

        fileMenu0 = tkinter.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=fileMenu0)
        fileMenu0.add_command(label="New Chart")
        profilesMenu0 = tkinter.Menu(menuBar, tearoff=0)
        profilesMenu0.add_command(label="Next")
        profilesMenu0.add_separator()
        profilesMenu0.add_command(label="Previous")
        profilesMenu0.add_separator()
        profilesMenu0.add_command(label="Save As")
        fileMenu0.add_command(label="Remove")
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Default")
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Market Overview")
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Symbol Information")
        fileMenu0.add_separator()
        fileMenu0.add_cascade(label="Profiles", menu=profilesMenu0)
        fileMenu0.add_separator()

        fileMenu0.add_command(label="Open ", command=Open)
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Save ", command=SaveAs, compound='left')
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Save As", command=SaveAs, compound='left')
        fileMenu0.add_separator()

        fileMenu0.add_command(label="Login to Trade")

        fileMenu0.add_command(label="Open a new account")
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Open Data Folder", command='openDataFolder', image='', compound='left')
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Print View")
        fileMenu0.add_separator()
        fileMenu0.add_command(label="Exit", command=exit)

        fileMenu1 = tkinter.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="View", menu=fileMenu1)
        fileMenu1.add_command(label="New Window")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="Titel Window")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="Title Horizontal Window")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="Title Vertical Window")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="Cascade View")

        fileMenu2 = tkinter.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Insert", menu=fileMenu2)

        indicatorMenu = tkinter.Menu(menuBar, tearoff=0)
        indicatorMenu.add_command(label="Accelerator Oscillator")

        indicatorMenu.add_command(label="Accumulation /Distribution")
        indicatorMenu.add_command(label="Alligator")
        indicatorMenu.add_command(label="Average Directional Movement index")
        indicatorMenu.add_command(label="CCI")
        indicatorMenu.add_command(label="Average True Ranges")
        indicatorMenu.add_command(label="Awesome Oscillator")
        indicatorMenu.add_separator()
        trendMenu = tkinter.Menu(indicatorMenu, tearoff=0)

        trendMenu.add_command(label="Bollinger Bands")
        trendMenu.add_command(label="Moving Average")
        trendMenu.add_command(label="SAR")
        trendMenu.add_command(label="RSI")
        trendMenu.add_command(label="Parabolic")

        indicatorMenu.add_cascade(label="Trend", menu=trendMenu)

        fileMenu2.add_cascade(label="Indicator", menu=indicatorMenu)
        fileMenu2.add_separator()
        fileMenu2.add_command(label="Titel Window")
        fileMenu2.add_separator()
        fileMenu2.add_command(label="Title Horizontal Window")
        fileMenu2.add_separator()
        fileMenu2.add_command(label="Title Vertical Window")
        fileMenu2.add_separator()
        fileMenu2.add_command(label="Cascade View")

        fileMenu3 = tkinter.Menu(menuBar, tearoff=0)
        fileMenu3.add_command(label="CandleStick chart")

        fileMenu3.add_command(label="Bar chart")

        fileMenu3.add_command(label="Line chart")

        fileMenu3.add_separator()
        fileMenu3.add_command(label="Foreground chart")
        fileMenu3.add_separator()

        fileMenu3.add_command(label="TimeFrame")

        fileMenu3.add_command(label="Template")
        fileMenu3.add_separator()

        fileMenu3.add_command(label="Grid")
        fileMenu3.add_command(label="Volumes")
        fileMenu3.add_command(label="Grid")
        fileMenu3.add_command(label="Auto Scroll")
        fileMenu3.add_separator()

        fileMenu3.add_command(label="Properties")

        menuBar.add_cascade(label="Chart", menu=fileMenu3)

        fileMenu4 = tkinter.Menu(menuBar, tearoff=0)

        fileMenu4.add_command(label="New Window")
        fileMenu4.add_separator()
        fileMenu4.add_command(label="Title Window")
        fileMenu4.add_separator()
        fileMenu4.add_command(label="Cascading Window")
        fileMenu4.add_separator()
        fileMenu4.add_command(label="Title Horizontal ")
        fileMenu4.add_separator()
        fileMenu4.add_command(label="Title Vertical")
        menuBar.add_cascade(label="Windows", menu=fileMenu4)

        fileMenu5 = tkinter.Menu(menuBar, tearoff=0)
        fileMenu5.add_command(label="History Center")
        fileMenu5.add_command(label="Global variables")
        fileMenu5.add_separator()
        fileMenu5.add_command(label="Options")

        menuBar.add_cascade(label="Tools", menu=fileMenu5)

        fileMenu6 = tkinter.Menu(menuBar, tearoff=0)
        fileMenu6.add_command(label="Help Center")
        fileMenu6.add_command(label="Updates")

        menuBar.add_cascade(label="Help", menu=fileMenu6)

        fileMenu7 = tkinter.Menu(menuBar, tearoff=0)
        fileMenu7.add_command(label="About Us")
        fileMenu7.add_command(label="Infos")
        menuBar.add_cascade(label="About", menu=fileMenu7)

        window.title("Blueyes                            " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        window.geometry("1530x780")

        window.mainloop()

    def openDataFolder() -> bool:
        return Dialog
