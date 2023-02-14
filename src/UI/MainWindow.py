import datetime
import tkinter
from msilib import Dialog
from tkinter import TOP, dialog
from tkinter.filedialog import SaveAs
from typing import Type

from Bueyes.src.BackEnd.Db import Db


# create a database


# create a window
def get_open_data_folder() -> bool:
    choice_box = tkinter.filedialog

    return True


def print_view():
    pass


def remove():
    pass


def market_overview():
    pass


def save():
    pass


def open_dialog():
    pass


def login_to_trade():
    pass


def open_account():
    pass


def titel_window():
    pass


def title_window():
    pass


def title_horizontal_window():
    pass


def title_vertical_window():
    pass


def cascade_view_window():
    pass


def get_candle_stick_chart():
    pass


def get_foreground():
    pass


def get_bar_chart():
    pass


def get_timeframe():
    pass


def get_line_chart():
    pass


def get_template():
    pass


def get_properties():
    pass


def get_auto_scroll():
    pass


def get_awesome_oscillator():
    pass


def get_moving_average():
    pass


def get_bollinger_bands():
    pass


def get_sar():
    pass


def get_parabolic():
    pass


def get_rsi():
    pass


def show(win_dow):
    win_dow.iconbitmap('./src/images/blueyes.ico')
    db = Db
    db.connect()

    menu_bar = tkinter.Menu(win_dow, border=30)

    case_panel = tkinter.PanedWindow(win_dow, border=100, background='brown', width=1500, height=700)

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
    profiles_menu0.add_command(label="Save As", command=SaveAs)
    file_menu0.add_command(label="Remove", command=lambda: remove())
    file_menu0.add_separator()
    file_menu0.add_command(label="Default")
    file_menu0.add_separator()
    file_menu0.add_command(label="Market Overview", command=lambda: market_overview())
    file_menu0.add_separator()
    file_menu0.add_command(label="Symbol Information")
    file_menu0.add_separator()
    file_menu0.add_cascade(label="Profiles", menu=profiles_menu0)
    file_menu0.add_separator()

    file_menu0.add_command(label="Open ", command=lambda: open_dialog(), compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Save ", command=lambda: save(), compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Save As", command=lambda: SaveAs, compound='left')
    file_menu0.add_separator()

    file_menu0.add_command(label="Login to Trade", command=lambda: login_to_trade(), compound='left')

    file_menu0.add_command(label="Open a new account", command=lambda: open_account(), compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Open Data Folder",
                           command=lambda: get_open_data_folder(), compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Print View", command=lambda: print_view(),compound='left')
    file_menu0.add_separator()
    file_menu0.add_command(label="Exit", command=exit, compound='right')

    file_menu1 = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=file_menu1)
    file_menu1.add_command(label="New Window", command=lambda: tkinter.PanedWindow())
    file_menu1.add_separator()
    file_menu1.add_command(label="Title Window", command=lambda: title_window())
    file_menu1.add_separator()
    file_menu1.add_command(label="Title Horizontal Window", command=lambda: title_horizontal_window())
    file_menu1.add_separator()
    file_menu1.add_command(label="Title Vertical Window", command=lambda: title_vertical_window())
    file_menu1.add_separator()
    file_menu1.add_command(label="Cascade View", command=lambda: cascade_view_window())

    file_menu2 = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Insert", menu=file_menu2)

    indicator_menu = tkinter.Menu(menu_bar, tearoff=0)
    indicator_menu.add_command(label="Accelerator Oscillator")

    indicator_menu.add_command(label="Accumulation /Distribution")
    indicator_menu.add_command(label="Alligator")
    indicator_menu.add_command(label="Average Directional Movement index")
    indicator_menu.add_command(label="CCI")
    indicator_menu.add_command(label="Average True Ranges")
    indicator_menu.add_command(label="Awesome Oscillator", command=lambda: get_awesome_oscillator())
    indicator_menu.add_separator()
    trend_menu = tkinter.Menu(indicator_menu, tearoff=0)

    trend_menu.add_command(label="Bollinger Bands",command=lambda: get_bollinger_bands())
    trend_menu.add_command(label="Moving Average",command=lambda: get_moving_average())
    trend_menu.add_command(label="SAR",command=lambda: get_sar())
    trend_menu.add_command(label="RSI",command=lambda: get_rsi())
    trend_menu.add_command(label="Parabolic",command=lambda: get_parabolic())

    indicator_menu.add_cascade(label="Trends", menu=trend_menu)

    file_menu2.add_cascade(label="Indicators", menu=indicator_menu)
    file_menu2.add_separator()
    file_menu2.add_command(label="Title ")
    file_menu2.add_separator()
    file_menu2.add_command(label="Title ")
    file_menu2.add_separator()
    file_menu2.add_command(label="Title ")
    file_menu2.add_separator()
    file_menu2.add_command(label="Ca")

    file_menu3 = tkinter.Menu(menu_bar, tearoff=0)
    file_menu3.add_command(label="CandleStick chart", command=lambda : get_candle_stick_chart())

    file_menu3.add_command(label="Bar chart", command=lambda : get_bar_chart())

    file_menu3.add_command(label="Line chart", command=lambda : get_line_chart())

    file_menu3.add_separator()
    file_menu3.add_command(label="Foreground chart", command=lambda: get_foreground())
    file_menu3.add_separator()

    file_menu3.add_command(label="TimeFrame", command=lambda: get_timeframe())

    file_menu3.add_command(label="Template", command=lambda: get_template())
    file_menu3.add_separator()

    file_menu3.add_command(label="Grid")
    file_menu3.add_command(label="Volumes")
    file_menu3.add_command(label="Grid")
    file_menu3.add_command(label="Auto Scroll",command=lambda: get_auto_scroll())
    file_menu3.add_separator()

    file_menu3.add_command(label="Properties", command=lambda x: get_properties())
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


