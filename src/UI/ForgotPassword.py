import tkinter

from src.Db import Db


def get_login_frame():
    pass


def get_valid_email(email):
    db = Db

    db.execute(param=email)

    pass


class ForgotPassword:

    def __init__(self, root):
        self.root = root
        tk_window = tkinter.Frame(root, padx=300, pady=35)

        # password label and password entry box
        tkinter.Label(tk_window, text="Email :").grid(row=1, column=0)

        email = tkinter.StringVar()
        tkinter.Entry(tk_window, textvariable=email).grid(row=1, column=1)

        tkinter.Button(tk_window, text="Submit", background="green", command=lambda: get_valid_email(email)).grid(row=6,
                                                                                                                  column=2)

        # login button
        tkinter.Button(tk_window, text="Go back", command=lambda: get_login_frame()).grid(row=6, column=0)
        # login button
        tk_window.pack()
