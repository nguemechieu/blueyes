import tkinter
from datetime import datetime
from doctest import master

from tkinter import Label, messagebox, X
from turtledemo.chaos import f


from Bueyes.Db import Db
from Bueyes.src.UI import Registration, ResetPassword
from Bueyes.src.UI.ForgotPassword import ForgotPassword
from Bueyes.src.UI.MainWindow import show


def validate_login(user_: str = '', pwd_: str = '') -> object:
    check_counter = None
    db_username_ = None
    db_password_ = None
    db = Db.connect()

    try:

        c = db.connect().cursor()

        for row in c.execute("Select * from users"):
            db_username_ = row[1]
            db_password_ = row[5]
    except Exception as ep:
        messagebox.showerror('Error', ep)

    if user_ == "":
        warn_ = "Username can't be empty"
    else:
        check_counter += 1

    if pwd_ == "":
        warn_ = "Password can't be empty"
    else:
        check_counter += 1

    if check_counter == 2:
        if user_ == db_username_ and pwd_ == db_password_:
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            show_pages('Main')

        else:
            messagebox.showerror('Login Status', 'invalid username or password')

    else:
        messagebox.showerror('', warn_)
        return db


def reset_pass(): pass


class UpdatePassword:
    @classmethod
    def show(cls):
        pass


def show_pages(page0):
    pages = ['Register', 'Forgot Password', 'Update Password', 'Reset Password', 'Login', 'Main', 'About']
    root = tkinter.Tk()
    root.iconify = True
    root.resizable = True
    root.image_names = ['blueyes.png']
    root.iconbitmap('../Bueyes/src/images/blueyes.ico')
    bgf = tkinter.PhotoImage(file='../Bueyes/src/images/blueyes.png')

    # Adjust size
    root.geometry("1530x780")
    if page0 == pages[0]:
        Registration.Registration(root=root)

    if page0 == pages[1]:
        ForgotPassword.show()

    if page0 == pages[2]:

        ResetPassword.show()

        if page0 == pages[3]:
            UpdatePassword.show()

    if page0 == pages[4]:
        r = LoginFrame()
        r.remember__me = False
    if page0 == pages[5]:
        show()


class LoginFrame(tkinter.Tk):

    def __init__(self, root, bgf=None):

        super().__init__()
        self.root = root
        self.bgf = bgf

        # Add image file
        root.title(string='Blueyes| Login            ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        master_ = tkinter.Frame(root, border=4, padx=400, background='black', height=780, pady=100, width=1530)
        master_.pack(side="left", fill=X)

        # username label and text entry box

        Label(master_, text="Username :", font=f).grid(row=0, column=0)
        usern_ = tkinter.StringVar()
        tkinter.Entry(master_, textvariable=usern_, font=f).grid(row=0, column=1)

        # password label and password entry box
        Label(master_, text="Password :", font=f).grid(row=1, column=0)

        passw_ = tkinter.StringVar()
        tkinter.Entry(master_, textvariable=passw_, font=f, show='*').grid(row=1, column=1)

        remember__me = tkinter.StringVar()
        tkinter.Checkbutton(master_, text='Remember me?', font=f, textvariable=remember__me).grid(row=2, column=1)

        # login button
        tkinter.Button(master_, width=15,
                       text='Login',
                       font=f,

                       cursor='hand2', command=lambda: validate_login(user_=usern_.get(), pwd_=passw_.get())).grid(
            row=6,
            column=2)

        # login button
        tkinter.Button(master_, text='Register',
                       font=f,
                       cursor='hand2', command=lambda: show_pages(page0='Register')).grid(row=6, column=0)
        # login button

        tkinter.Button(master_, text="Forgot Password", background='purple', font=f,

                       command=lambda: show_pages(page0='Forgot Password')).grid(row=9, column=1)
