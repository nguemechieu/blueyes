import json
import tkinter
from tkinter import TOP

from src.BackEnd.Connexion.RequestHandler import RequestHandler


class News(object):

    def __init__(self, title, country, impact, forecast, previous):
        self.title = title
        self.country = country
        self.impact = impact
        self.forecast = forecast
        self.previous = previous

    @staticmethod
    def get() -> object:
        urls = "http://nfs.faireconomy.media/ff_calendar_thisweek.json?version=74f11aed5c03a2a90fca2a09a68e03b9"

        r =RequestHandler(url0=urls). make_request()
        return json.loads(r)

    @classmethod
    def show(cls) -> None:
        cl = tkinter.Tk()
        menubar = tkinter.Menu(cl, background='brown')

        cl.config(menu=menubar, background='green')

        panel = tkinter.PanedWindow(cl)
        list_view = tkinter.Listbox(cl)

        list_view.pack(side=TOP)
        panel.pack()
        panel.add(label='news')

        cl.mainloop()

        return
