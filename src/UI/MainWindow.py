import glob
import logging
import os
import random
import tkinter
from tkinter import filedialog, BOTTOM, LEFT, X, TOP
from tkinter.filedialog import Open, SaveAs
from typing import Type

import pandas as pd

global i, colors, buy_sell_btn,timeframe_btn_list, hy, xcolor, toolbar2
logger = logging.getLogger(__name__)
def get_new_window():
    pass

class MainWindow:
    def __init__(self, root:tkinter.Tk=None):



        global toolbar2_, hy, hyl, toolbar, timeframe_btn_list_
        self.root = root
        # Settings main window

        # Initialize the database
        xcolor_ = 'black'

        # Create a Menu

        win_dow = tkinter.Frame(self.root)

        win_dow.rowconfigure(0, weight=1)
        win_dow.columnconfigure(0, weight=1)

        win_dow.bbox(row=6, column=3)
        canvas= tkinter.Canvas(master=self.root, takefocus=3, bg='black', borderwidth=1000, border=12, width=1000, height=500, selectbackground='blue')
        canvas.pack()

        menu_bar = tkinter.Menu(self.root, border=30)
        self.root.config(menu=menu_bar, padx=8, takefocus=9)  # menu bar
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
        file_menu2.add_command(label="mv ")
        file_menu2.add_separator()
        file_menu2.add_command(label="cci ")
        file_menu2.add_separator()
        file_menu2.add_command(label="TR ")
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

        time_frame=pd.read_csv( "oanda__granularity.csv")

        print("\n================================\n" + str(time_frame.items()))



        for hyl in time_frame:
           print("\n================================\n" + str(hyl))

           timeframe_btn_list_ = tkinter.Button(self.root, text=str(hyl))
           toolbar = tkinter.Frame(root, takefocus=2, border=2, background='blue' )
           toolbar.pack(side=TOP, ipadx=2)
           timeframe_btn_list_=[timeframe_btn_list_]


        for timeframe in timeframe_btn_list_:
            colors_ = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'brown', 'yellow', 'lime', 'gold']
            x0 = int(random.random() * 10)
            if x0 < 10:
                xcolor_ = colors_[x0]
            timeframe_btn = tkinter.Button(toolbar, text=str(timeframe), border=2, height=2, width=2, background=xcolor_)

            if timeframe == 'Zoom -':
                timeframe_btn = tkinter.Button(toolbar, text='ZOOM', border=2, height=2, width=2,
                                               bitmap='/src/images/folder.png',
                                               background=xcolor_)
            timeframe_btn.pack(side=LEFT, fill=X, ipadx=2, padx=2, pady=2)

            tkinter.Label(root, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
            tkinter.Label(root, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
            tkinter.Label(root, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)

            # Create toolbar for managing candle stick events and trades
            toolbar2_ = tkinter.Frame(root, borderwidth=2, height=2, padx=2, pady=2, highlightcolor='black')
            toolbar2_.pack(side=BOTTOM, ipadx=2, padx=2, pady=2, expand=3, ipady=2)

        btn_list = ['BUY', 'SELL', 'Trailing Buy', 'Trailing Sell', 'Close All']

        for i__ in btn_list:
            colors_ = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'brown', 'yellow', 'lime', 'gold']
            x0 = int(random.random() * 10)

            if x0 < 10:
                xcolor_ = colors_[x0]

                buy_sell_btn_ = tkinter.Button(toolbar2_, text=i__, background=xcolor_,
                                               relief='raised',
                                               border=2, width=2,
                                               padx=3, pady=2,
                                               takefocus=3,
                                               justify='center')
                buy_sell_btn_.pack(side=LEFT, ipadx=2, ipady=2, padx=2)


















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


def get_about_us():
    pass


def dic_imgs():
    imgss = {}
    for df in glob.glob("images/*.png"):
        pathfile = df
        df = os.path.basename(df)
        name = df.split(".")[0]
        imgss[name] = tkinter.PhotoImage(file=pathfile)
        if name == "folder":
            imgss[name] = imgss[name].subsample(2)


def get_open_data_folder() -> Type[Open]:
    choice_box = filedialog.Open
    return choice_box


def callback():
    print("called the callback!")

    pass

# --------------------------------
################################
# This Class is responsible for displaying Main Window
