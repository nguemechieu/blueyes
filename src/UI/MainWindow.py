import datetime
import glob
import os
import random
import tkinter
from tkinter import filedialog, BOTTOM, LEFT, X, TOP
from tkinter.filedialog import Open, SaveAs
from typing import Type

from Bueyes.src.UI.CandleStickChart import CandleStickChart


def get_new_window():
    pass


class MainWindow(object):

    def __init__(self, root=None):

        self.root = root
        # Settings main window

        # Initialize the database

        global i, colors, buy_sell_btn, toolbar2

        xcolor = 'black'

        # Create a Menu
        root0 = root
        win_dow = tkinter.Frame(root0)

        win_dow.rowconfigure(0, weight=1)
        win_dow.columnconfigure(0, weight=1)

        win_dow.bbox(row=6, column=3)

        menu_bar = tkinter.Menu(win_dow, border=30)
        root0.config(menu=menu_bar, padx=8, takefocus=9)  # menu bar
        file_menu0 = tkinter.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu0)
        file_menu0.add_command(label="New Chart")
        profiles_menu0 = tkinter.Menu(menu_bar, tearoff=0)
        profiles_menu0.add_command(label="Next")
        profiles_menu0.add_separator()
        profiles_menu0.add_command(label="Previous")
        profiles_menu0.add_separator()

        profiles_menu0.add_command(label="Save As", command=SaveAs)

        file_menu0.add_separator()
        file_menu0.add_command(label="Market Overview", command=lambda: market_overview)
        file_menu0.add_separator()
        file_menu0.add_cascade(label="Profiles", menu=profiles_menu0)
        file_menu0.add_separator()
        file_menu0.add_command(label="Open ", command=lambda: open_dialog, compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Save ", command=lambda: save, compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Save As", command=lambda: SaveAs, compound='left')
        file_menu0.add_separator()

        file_menu0.add_command(label="Login to Trade", command=lambda: login_to_trade, compound='left')

        file_menu0.add_command(label="Open a new account", command=lambda: open_account(root=win_dow), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Open Data Folder",
                               command=lambda: get_open_data_folder, compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Print View", command=lambda: print_view(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Exit", command=exit, compound='right')

        file_menu1 = tkinter.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu1)
        file_menu1.add_command(label="New Window", command=lambda: get_new_window)
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Window", command=lambda: title_window)
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Horizontal Window", command=lambda: title_horizontal_window)
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Vertical Window", command=lambda: title_vertical_window)
        file_menu1.add_separator()
        file_menu1.add_command(label="Cascade View", command=lambda: cascade_view_window)
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
        trend_menu.add_command(label="Bollinger Bands", command=lambda: get_bollinger_bands)
        trend_menu.add_command(label="Moving Average", command=lambda: get_moving_average)
        trend_menu.add_command(label="SAR", command=lambda: get_sar())
        trend_menu.add_command(label="RSI", command=lambda: get_rsi())
        trend_menu.add_command(label="Parabolic", command=lambda: get_parabolic)

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
        file_menu3.add_command(label="CandleStick chart", command=lambda: get_candle_stick_chart)

        file_menu3.add_command(label="Bar chart", command=lambda: get_bar_chart)

        file_menu3.add_command(label="Line chart", command=lambda: get_line_chart())

        file_menu3.add_separator()
        file_menu3.add_command(label="Foreground chart", command=lambda: get_foreground)
        file_menu3.add_separator()

        file_menu3.add_command(label="TimeFrame", command=lambda: get_timeframe)

        file_menu3.add_command(label="Template", command=lambda: get_template)
        file_menu3.add_separator()

        file_menu3.add_command(label="Grid")
        file_menu3.add_command(label="Volumes")
        file_menu3.add_command(label="Grid")
        file_menu3.add_command(label="Auto Scroll", command=lambda: get_auto_scroll)
        file_menu3.add_separator()

        file_menu3.add_command(label="Properties", command=lambda x: get_properties)
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
        file_menu7.add_command(label="About Us", command=lambda: get_about_us)
        file_menu7.add_command(label="Info's")
        menu_bar.add_cascade(label="About", menu=file_menu7)

        # Creating and displaying label for toolbar
        timeframe_btn_list = ['M1', 'M5', 'M15', 'M30', 'H1', 'H2', 'H4', 'H6', 'H12', 'W', 'M', 'Y',
                              'Zoom -', 'Zoom +', 'Candle Stick', 'Line', 'Strategy tester'

                              ]

        # Create sub window

        toolbar = tkinter.Frame(win_dow, relief="raised", takefocus=2, border=2, background='blue'

                                )
        toolbar.pack(side=TOP, ipadx=2)
        for timeframe in timeframe_btn_list:
            colors = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'brown', 'yellow', 'lime', 'gold']
            x0 = int(random.random() * 10)
            if x0 < 10:
                xcolor = colors[x0]
            timeframe_btn = tkinter.Button(toolbar, text=timeframe, border=2, height=2, width=2, background=xcolor)

            if timeframe_btn_list.index(timeframe) == 'Zoom -':
                timeframe_btn = tkinter.Button(toolbar, text=timeframe, border=2, height=2, width=2,
                                               bitmap='/src/images/folder.png',
                                               background=xcolor)
            timeframe_btn.pack(side=LEFT, fill=X, ipadx=2, padx=2, pady=2)

            # tkinter.Label(sub_window, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
            # tkinter.Label(sub_window, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
            # tkinter.Label(sub_window, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)

            # Create toolbar for managing candle stick events and trades
            toolbar2 = tkinter.Frame(win_dow, borderwidth=2, height=2, padx=2, pady=2, highlightcolor='black')
            toolbar2.pack(side=BOTTOM, ipadx=2, padx=2, pady=2, expand=3, ipady=2)
        btn_list = ['BUY', 'SELL', 'Trailing Buy', 'Trailing Sell', 'Close All']

        for i in btn_list:
            colors = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'brown', 'yellow', 'lime', 'gold']
            x0 = int(random.random() * 10)

            if x0 < 10:
                xcolor = colors[x0]

                buy_sell_btn = tkinter.Button(toolbar2, text=i, background=xcolor,
                                              relief='raised',
                                              border=2, width=2,
                                              padx=3, pady=2,
                                              takefocus=3,
                                              justify='center')
                buy_sell_btn.pack(side=LEFT, ipadx=2, ipady=2, padx=2)

        # Main loop for displaying

        sub_window = tkinter.Frame(root)

        CandleStickChart(sub_window)

        # tkinter.Canvas(sub_window, background='black', borderwidth=10, width=1100, height=300, border=12,
        #   relief='raised')

        sub_window.pack(side=LEFT, ipadx=7, fill=X)


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


def open_account(root):
    frame = tkinter.Frame(root)
    frame.pack(side=LEFT, ipadx=2, ipady=3)

    CandleStickChart(root)

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


def get_about_us(self):
    pass


def dic_imgs():
    imgss = {}
    for i in glob.glob("images/*.png"):
        pathfile = i
        i = os.path.basename(i)
        name = i.split(".")[0]
        imgss[name] = tkinter.PhotoImage(file=pathfile)
        if name == "folder":
            imgss[name] = imgss[name].subsample(2)


def get_open_data_folder() -> Type[Open]:
    choice_box = filedialog.Open
    return choice_box


def callback():
    print("called the callback!")

# --------------------------------
################################
# This Class is responsible for displaying Main Window
