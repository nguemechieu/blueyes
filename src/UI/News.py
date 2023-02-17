import tkinter
from tkinter import TOP

from self import self

from Bueyes.src.BackEnd.Connexion.RequestHandler import make_request


class News(object):

    def __init__(self, title, country, impact, forecast, previous):
        self.title = title
        self.country = country
        self.impact = impact
        self.forecast = forecast
        self.previous = previous

    @staticmethod
    def get(data0='') -> object:
        urls = "http://nfs.faireconomy.media/ff_calendar_thisweek.json?version=74f11aed5c03a2a90fca2a09a68e03b9"
        method = "GET"
        ap_i = "123456gjo"
        r = make_request(self, method, ap_i, urls, data0)
        return r.json()

    @classmethod
    def show(cls) -> None:
        cls = tkinter.Tk()
        menubar = tkinter.Menu(cls, background='brown')

        cls.config(menu=menubar, background='green')

        panel = tkinter.PanedWindow(cls)
        list_view = tkinter.Listbox(cls)

        list_view.pack(side=TOP)
        panel.pack()
        panel.add(label='news')

        cls.mainloop()

        return
