import tkinter
from tkinter import X


class MarketDataWindow(object):

    @staticmethod
    def show() :
        win_dow = tkinter.PanedWindow()

        canvas = tkinter.Canvas(background='black', border=7, borderwidth=70, width=1000, takefocus=9)

        win_dow.add(child=canvas)
        
        win_dow.pack(side="left", fill=X)



