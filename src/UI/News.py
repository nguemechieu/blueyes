import tkinter
from cProfile import label

import requests


class News(object):

    def __init__(self, title, country, impact, forecast, previous):
        self.title = title
        self.country = country
        self.impact = impact
        self.forecast = forecast
        self.previous = previous

    @staticmethod
    def get() -> object:
        request = requests.Request
        request.url = 'https://nfs.faireconomy.media/ff_calendar_thisweek.json?version=74f11aed5c03a2a90fca2a09a68e03b9'
        request.method = 'GET'
        response = requests.request(url=request.url, params=request.method, headers=request.headers, timeout=5000)

        return response.json()

    @staticmethod
    def show() -> None:
        win_dow = tkinter.Tk()
        menubar = tkinter.Menu(win_dow, background='brown')

        win_dow.config(menu=menubar, background='green')

        panel = tkinter.PanedWindow(win_dow)
        panel.pack()
        panel.add(label='news')

        win_dow.mainloop()

        return
