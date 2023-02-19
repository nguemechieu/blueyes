import json
import tkinter
from tkinter import TOP

from src.BackEnd.Connexion.JsonToCsv import JsonToCsv
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
        urls = "http://nfs.faireconomy.media"

        r =RequestHandler(url0=urls,api_key='')
        data=r.make_request(path='/ff_calendar_thisweek.json?version=74f11aed5c03a2a90fca2a09a68e03b9')

        print('News feed'+ data.__str__())



        with open("News.json", "w") as outfile: json.dump(data, outfile,sort_keys=True,indent=2)

        JsonToCsv().convert('News.json','News.csv')

        return data

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
