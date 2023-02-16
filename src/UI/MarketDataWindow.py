import tkinter
from distutils.command.config import config
from tkinter import X


class MarketDataWindow(object):

    @staticmethod
    def show() -> None:
        win_dow = tkinter.PanedWindow()

        canvas = tkinter.Canvas(background='black', border=7, borderwidth=70, width=1000, takefocus=9)

        win_dow.add(child=canvas)
        canvas.pack(fill=X, padx=9, ipadx=8, pady=9)
        win_dow.pack(side="left", fill=X)



