import tkinter
from datetime import datetime


def show_frame(frame):
    window = tkinter.Tk("Blueyes | Login                 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    window.config(menu=frame)

    window.geometry = '1530*780'
    window.mainloop()

    return None


class Navigator(object):
    pass
