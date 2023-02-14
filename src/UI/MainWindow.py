import datetime
import tkinter
from msilib import Dialog
from tkinter import TOP, dialog
from tkinter.filedialog import Open, SaveAs
from typing import Type

from pandas import options

from Bueyes.src.BackEnd.Db import Db


# create a database


# create a window
def get_open_data_folder() -> bool:
    choice_box = tkinter.filedialog

    return True


def show(win_dow):
    win_dow.iconbitmap('./src/images/blueyes.ico')
    db = Db
    db.connect()

    menu_bar = tkinter.Menu(win_dow, border=30)

    case_panel = tkinter.PanedWindow(win_dow, border=100, background='brown', width=1000, height=700)

    case_panel.pack()

    # Creating and displaying label for toolbar
    toolbar = tkinter.Label(win_dow)
    toolbar.pack(side=TOP)

    # Creating and displaying of Bold button
    bold_btn = tkinter.Button(toolbar, text="Bold")
    bold_btn.grid(row=0, column=0, padx=5)

    # Creating and displaying of italic button
    italic_btn = tkinter.Button(toolbar, text="Italic")
    italic_btn.grid(row=0, column=1, padx=5)
    timeframe_btn_list = ['M1', 'M5', 'M15', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'W', 'M', 'Y']

    for timeframe in timeframe_btn_list:
        timeframe_btn = tkinter.Button(win_dow, text=timeframe)

        case_panel.add(timeframe_btn)

    # toolBar = tkinter.Tool(window)

    win_dow.config(menu=menu_bar, borderwidth=20, border=12)

    dashboard = tkinter.Frame(win_dow)
    dashboard.pack()
    canvas = tkinter.Canvas(dashboard, border=200, background='black', closeenough=80, width=1000)
    canvas.pack()

    flow_panel = tkinter.Spinbox(win_dow)
    flow_panel.pack()

    case_panel.add(dashboard)
    auto_trading = tkinter.Button(dashboard, text="Auto Trading", pady=10, command=lambda: tkinter.Label())
    auto_trading.pack()

    file_menu0 = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu0)
    file_menu0.add_command(label="New Chart")
    profiles_menu0 = tkinter.Menu(menu_bar, tearoff=0)
    profiles_menu0.add_command(label="Next")
    profiles_menu0.add_separator()
    profiles_menu0.add_command(label="Previous")
    profiles_menu0.add_separator()
    profiles_menu0.add_command(label="Save As")
    file_menu0.add_command(label="Remove")
    file_menu0.add_separator()
    file_menu0.add_command(label="Default")
    file_menu0.add_separator()
    file_menu0.add_command(label="Market Overview")
    file_menu0.add_separator()
    file_menu0.add_command(label="Symbol Information")
    file_menu0.add_separator()
    file_menu0.add_cascade(label="Profiles", menu=profiles_menu0)
    file_menu0.add_separator()

    file_menu0.add_command(label="Open ", command=Open)
    file_menu0.add_separator()
    file_menu0.add_command(label="Save ", command=SaveAs, compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Save As", command=SaveAs, compound='left')
    file_menu0.add_separator()

    file_menu0.add_command(label="Login to Trade")

    file_menu0.add_command(label="Open a new account")
    file_menu0.add_separator()
    file_menu0.add_command(label="Open Data Folder",
                           command=lambda: get_open_data_folder())
    file_menu0.add_separator()
    file_menu0.add_command(label="Print View")
    file_menu0.add_separator()
    file_menu0.add_command(label="Exit", command=exit)

    file_menu1 = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=file_menu1)
    file_menu1.add_command(label="New Window")
    file_menu1.add_separator()
    file_menu1.add_command(label="Titel Window")
    file_menu1.add_separator()
    file_menu1.add_command(label="Title Horizontal Window")
    file_menu1.add_separator()
    file_menu1.add_command(label="Title Vertical Window")
    file_menu1.add_separator()
    file_menu1.add_command(label="Cascade View")

    file_menu2 = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Insert", menu=file_menu2)

    indicator_menu = tkinter.Menu(menu_bar, tearoff=0)
    indicator_menu.add_command(label="Accelerator Oscillator")

    indicator_menu.add_command(label="Accumulation /Distribution")
    indicator_menu.add_command(label="Alligator")
    indicator_menu.add_command(label="Average Directional Movement index")
    indicator_menu.add_command(label="CCI")
    indicator_menu.add_command(label="Average True Ranges")
    indicator_menu.add_command(label="Awesome Oscillator")
    indicator_menu.add_separator()
    trend_menu = tkinter.Menu(indicator_menu, tearoff=0)

    trend_menu.add_command(label="Bollinger Bands")
    trend_menu.add_command(label="Moving Average")
    trend_menu.add_command(label="SAR")
    trend_menu.add_command(label="RSI")
    trend_menu.add_command(label="Parabolic")

    indicator_menu.add_cascade(label="Trend", menu=trend_menu)

    file_menu2.add_cascade(label="Indicator", menu=indicator_menu)
    file_menu2.add_separator()
    file_menu2.add_command(label="Titel Window")
    file_menu2.add_separator()
    file_menu2.add_command(label="Title Horizontal Window")
    file_menu2.add_separator()
    file_menu2.add_command(label="Title Vertical Window")
    file_menu2.add_separator()
    file_menu2.add_command(label="Cascade View")

    file_menu3 = tkinter.Menu(menu_bar, tearoff=0)
    file_menu3.add_command(label="CandleStick chart")

    file_menu3.add_command(label="Bar chart")

    file_menu3.add_command(label="Line chart")

    file_menu3.add_separator()
    file_menu3.add_command(label="Foreground chart")
    file_menu3.add_separator()

    file_menu3.add_command(label="TimeFrame")

    file_menu3.add_command(label="Template")
    file_menu3.add_separator()

    file_menu3.add_command(label="Grid")
    file_menu3.add_command(label="Volumes")
    file_menu3.add_command(label="Grid")
    file_menu3.add_command(label="Auto Scroll")
    file_menu3.add_separator()

    file_menu3.add_command(label="Properties")

    menu_bar.add_cascade(label="Chart", menu=file_menu3)

    file_menu4 = tkinter.Menu(menu_bar, tearoff=0)

    file_menu4.add_command(label="New Window")
    file_menu4.add_separator()
    file_menu4.add_command(label="Title Window")
    file_menu4.add_separator()
    file_menu4.add_command(label="Cascading Window")
    file_menu4.add_separator()
    file_menu4.add_command(label="Title Horizontal ")
    file_menu4.add_separator()
    file_menu4.add_command(label="Title Vertical")
    menu_bar.add_cascade(label="Windows", menu=file_menu4)

    file_menu5 = tkinter.Menu(menu_bar, tearoff=0)
    file_menu5.add_command(label="History Center")
    file_menu5.add_command(label="Global variables")
    file_menu5.add_separator()
    file_menu5.add_command(label="Options")

    menu_bar.add_cascade(label="Tools", menu=file_menu5)

    file_menu6 = tkinter.Menu(menu_bar, tearoff=0)
    file_menu6.add_command(label="Help Center")
    file_menu6.add_command(label="Updates")

    menu_bar.add_cascade(label="Help", menu=file_menu6)

    file_menu7 = tkinter.Menu(menu_bar, tearoff=0)
    file_menu7.add_command(label="About Us")
    file_menu7.add_command(label="Infos")
    menu_bar.add_cascade(label="About", menu=file_menu7)

    win_dow.title("Blueyes                            " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    win_dow.geometry("1530x780")
    win_dow.mainloop()


class MainWindow(object):

    def __init__(self, title): self.title = title

    @staticmethod
    def open_data_folder() -> Type[Dialog]:
        return Dialog

    MainWindow = tkinter.Tk()
    show(MainWindow)
