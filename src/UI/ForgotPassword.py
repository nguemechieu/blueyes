import tkinter

import mysql.connector

from Bueyes.src.BackEnd.configparser.ConfigParser import read_db_config


def get_login_frame():
    pass


def get_valid_email(email):
    db = mysql.connector.MySQLConnection
    db.connect(**read_db_config())
    db.find_one(email)

    pass


class ForgotPassword(object):

    @staticmethod
    def show() -> None:
        root = tkinter.Tk()

        root.geometry('1530x780')
        root.title('Blueyes | ForgotPassword  - blueyes.org')

        tk_window = tkinter.Frame(root, padx=300, height=300, pady=200)
        tk_window.pack()
        # password label and password entry box
        tkinter.Label(tk_window, text="Email :").grid(row=1, column=0)

        email = tkinter.StringVar()
        tkinter.Entry(tk_window, textvariable=email).grid(row=1, column=1)

        tkinter.Button(tk_window, text="Submit", background="green", command=lambda: get_valid_email(email)).grid(row=6, column=2)

        # login button
        tkinter.Button(tk_window, text="Go back", command=lambda: get_login_frame()).grid(row=6, column=0)
    # login button
