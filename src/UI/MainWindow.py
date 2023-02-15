import datetime
import glob

import os
import random
import tkinter
from email.mime import image

from tkinter import TOP, dialog, FLAT, LEFT, X, CENTER, BOTTOM

from tkinter.filedialog import SaveAs

from PIL.ImageOps import scale
from numpy import save

from Bueyes.src.BackEnd.Db import Db


class MainWindow(object):

    @staticmethod
    def get_open_data_folder() -> bool:
        choice_box = tkinter.filedialog
        return True

    def print_view(self):
        pass

    def remove(self):
        pass

    def market_overview(self):
        pass

    def save(self):
        pass

    def open_dialog(self):
        pass

    def login_to_trade(self):
        pass

    def open_account(self):
        pass

    def titel_window(self):
        pass

    def title_window(self):
        pass

    def title_horizontal_window(self):
        pass

    def title_vertical_window(self):
        pass

    def cascade_view_window(self):
        pass

    def get_candle_stick_chart(self):
        pass

    def get_foreground(self):
        pass

    def get_bar_chart(self):
        pass

    def get_timeframe(self):
        pass

    def get_line_chart(self):
        pass

    def get_template(self):
        pass

    def get_properties(self):
        pass

    def get_auto_scroll(self):
        pass

    def get_awesome_oscillator(self):
        pass

    def get_moving_average(self):
        pass

    def get_bollinger_bands(self):
        pass

    def get_sar(self):
        pass

    def get_parabolic(self):
        pass

    def get_rsi(self):
        pass

    def get_about_us(self):
        pass

    @staticmethod
    def dic_imgs():

        imgss = {}
        for i in glob.glob("images/*.png"):
            pathfile = i
            i = os.path.basename(i)
            name = i.split(".")[0]
            imgss[name] = tkinter.PhotoImage(file=pathfile)
            if name == "folder":
                imgss[name] = imgss[name].subsample(2)

    @staticmethod
    def callback():
        print("called the callback!")

    # --------------------------------
    ################################

    # This Class is responsible for displaying Main Window

    def show(self):
        # Initialize the database

        global i, colors, buy_sell_btn
        db = Db

        db.connect()

        xcolor = 'black'

        # Create a Menu
        win_dow = tkinter.Tk(screenName="Blueyes", baseName='blue')
        menu_bar = tkinter.Menu(win_dow, border=30)
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
        file_menu0.add_command(label="Market Overview", command=lambda: self.market_overview())
        file_menu0.add_separator()
        file_menu0.add_cascade(label="Profiles", menu=profiles_menu0)
        file_menu0.add_separator()
        file_menu0.add_command(label="Open ", command=lambda: self.open_dialog(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Save ", command=lambda: save(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Save As", command=lambda: SaveAs, compound='left')
        file_menu0.add_separator()

        file_menu0.add_command(label="Login to Trade", command=lambda: self.login_to_trade(), compound='left')

        file_menu0.add_command(label="Open a new account", command=lambda: self.open_account(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Open Data Folder",
                               command=lambda: self.get_open_data_folder(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Print View", command=lambda: self.print_view(), compound='left')
        file_menu0.add_separator()
        file_menu0.add_command(label="Exit", command=exit, compound='right')

        file_menu1 = tkinter.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu1)
        file_menu1.add_command(label="New Window", command=lambda: tkinter.PanedWindow())
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Window", command=lambda: self.title_window())
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Horizontal Window", command=lambda: self.title_horizontal_window())
        file_menu1.add_separator()
        file_menu1.add_command(label="Title Vertical Window", command=lambda: self.title_vertical_window())
        file_menu1.add_separator()
        file_menu1.add_command(label="Cascade View", command=lambda: self.cascade_view_window())
        file_menu2 = tkinter.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Insert", menu=file_menu2)
        indicator_menu = tkinter.Menu(menu_bar, tearoff=0)
        indicator_menu.add_command(label="Accelerator Oscillator")
        indicator_menu.add_command(label="Accumulation /Distribution")
        indicator_menu.add_command(label="Alligator")
        indicator_menu.add_command(label="Average Directional Movement index")
        indicator_menu.add_command(label="CCI")
        indicator_menu.add_command(label="Average True Ranges")
        indicator_menu.add_command(label="Awesome Oscillator", command=lambda: self.get_awesome_oscillator())
        indicator_menu.add_separator()
        trend_menu = tkinter.Menu(indicator_menu, tearoff=0)
        trend_menu.add_command(label="Bollinger Bands", command=lambda: self.get_bollinger_bands())
        trend_menu.add_command(label="Moving Average", command=lambda: self.get_moving_average())
        trend_menu.add_command(label="SAR", command=lambda: self.get_sar())
        trend_menu.add_command(label="RSI", command=lambda: self.get_rsi())
        trend_menu.add_command(label="Parabolic", command=lambda: self.get_parabolic())

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
        file_menu3.add_command(label="CandleStick chart", command=lambda: self.get_candle_stick_chart())

        file_menu3.add_command(label="Bar chart", command=lambda: self.get_bar_chart())

        file_menu3.add_command(label="Line chart", command=lambda: self.get_line_chart())

        file_menu3.add_separator()
        file_menu3.add_command(label="Foreground chart", command=lambda: self.get_foreground())
        file_menu3.add_separator()

        file_menu3.add_command(label="TimeFrame", command=lambda: self.get_timeframe())

        file_menu3.add_command(label="Template", command=lambda: self.get_template())
        file_menu3.add_separator()

        file_menu3.add_command(label="Grid")
        file_menu3.add_command(label="Volumes")
        file_menu3.add_command(label="Grid")
        file_menu3.add_command(label="Auto Scroll", command=lambda: self.get_auto_scroll())
        file_menu3.add_separator()

        file_menu3.add_command(label="Properties", command=lambda x: self.get_properties())
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
        file_menu7.add_command(label="About Us", command=lambda: self.get_about_us())
        file_menu7.add_command(label="Info's")
        menu_bar.add_cascade(label="About", menu=file_menu7)

        # Settings main window
        win_dow.title("Blueyes                            " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        win_dow.geometry("1530x780")
        win_dow.config(menu=menu_bar, padx=8, takefocus=9)  # menu bar

        # Creating and displaying label for toolbar
        timeframe_btn_list = ['M1', 'M5', 'M15', 'M30', 'H1', 'H2', 'H4', 'H6', 'H12', 'W', 'M', 'Y',
                              'Zoom -', 'Zoom +', 'Candle Stick', 'Line', 'Strategy tester'

                              ]

        # Create sub window
        sub_window = tkinter.PanedWindow(win_dow)
        toolbar = tkinter.Frame(sub_window, relief="raised", width=1000, takefocus=2, border=2,

                                highlightcolor="green")
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

        spinner = tkinter.Spinbox(sub_window, increment=0.01,
                                  buttonuprelief='raised', border=1, width=10,
                                  borderwidth=2,
                                  background="green")

        spinner.pack(side=TOP, pady=2)

        # Create canvas to display candle sticks chart

        canvas = tkinter.Canvas(sub_window, border=2, width=1200, relief='raised', background='black', borderwidth=2,
                                height=400)
        # tkinter.Label(sub_window, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
        # tkinter.Label(sub_window, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
        # tkinter.Label(sub_window, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)

        # Create toolbar for managing candle stick events and trades

        toolbar2 = tkinter.Frame(sub_window, borderwidth=2, height=2, padx=2, pady=2, highlightcolor='black')

        toolbar2.pack(side=BOTTOM, ipadx=2, padx=2, pady=2, expand=3, ipady=2)

        btn_list = ['BUY', 'SELL', 'Trailing Buy', 'Trailing Sell', 'Close All']

        twi_ker = tkinter.Listbox(sub_window, borderwidth=1300, border=2, relief='raised')
        twi_ker.pack(side=LEFT, ipadx=2, ipady=2)
        for i in btn_list:

            colors = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'brown', 'yellow', 'lime', 'gold']

            x0 = int(random.random() * 10)

            if x0 < 10: xcolor = colors[x0]

            buy_sell_btn = tkinter.Button(toolbar2, text=i, background=xcolor,
                                          relief='raised',
                                          border=2, width=2,
                                          padx=3, pady=2,
                                          takefocus=3,
                                          justify='center')

            buy_sell_btn.pack(side=LEFT, ipadx=2, ipady=2, padx=2)

            canvas.pack()

            # Display All objects
            sub_window.pack()

        # Main loop for displaying
        win_dow.iconbitmap('./src/images/blueyes.ico')
        win_dow.mainloop()
        return
