import tkinter
from email.mime import image
from tkinter import X

from self import self


class CandleStickChart(object):

    def __init__(self, windows=tkinter.Misc()):
        canvas = tkinter.Canvas(windows, background='black', borderwidth=1000, width=1100, height=300, border=12, relief='raised' )
        canvas.pack(fill=X, side='left', padx=350, pady=8)
        windows.pack_slaves()

