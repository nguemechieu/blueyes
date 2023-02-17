import datetime
import tkinter

from tkinter import Label, messagebox, X, Tk
from turtledemo.chaos import f

from src.Db import Db
from src.UI import ResetPassword, Registration
from src.UI.ForgotPassword import ForgotPassword
from src.UI.MainWindow import MainWindow


class UpdatePassword:
    pass


def show_pages(page0):
    pages = ['Register', 'Forgot Password', 'Update Password', 'Reset Password', 'Login', 'Main', 'About']

    root0: Tk = tkinter.Tk()
    root = tkinter.Frame(root0, border=9)
    root.pack()
    # Add image file
    root0.title('Blueyes| Login            ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    root.iconify = True
    root.resizable = True
    root.image_names = ['blueyes.png']
    root0.iconbitmap('images/blueyes.ico')
    # Adjust size
    root0.geometry("1530x780")

    if page0 == pages[0]:
        root.forget()

        root0.title('Blueyes| Registration           ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        Registration.Registration(root0)

    if page0 == pages[1]:
        root.destroy()

        root0.geometry('1530x780')
        root0.title('Blueyes | ForgotPassword  - blueyes.org')

        ForgotPassword(root=root0)

    if page0 == pages[2]:
        root.destroy()
        ResetPassword.show()

    if page0 == pages[3]:
        root.forget()
        UpdatePassword.show()
    if page0 == pages[4]:
        root.destroy()
        root = tkinter.Frame(root0)
        root.pack()
        root.iconify = True
        root.resizable = True
        root0.image_names = ['blueyes.png']
        root0.iconbitmap('images/blueyes.ico')
        bgf = tkinter.PhotoImage(file='images/blueyes.png')
        r = LoginFrame(root=root)

        r.remember__me = False

    if page0 == pages[5]:
        root.destroy()
        root0.title("Blueyes| Dashboard                           " + datetime.datetime.now().strftime("%Y-%m-%d "
                                                                                                      "%H:%M:%S"))
        root0.geometry("1530x780")

        MainWindow(root0)

    root.mainloop()


def validate_login(user_: str ='', pwd_: str=''):
    warn_ : str="Please enter your username and password"
    db_username_: str=""
    db_password_: str=""
    check_counter = None

    try:

        c = Db()

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
    show_pages('Main')
    if check_counter == 2:
        if user_ == db_username_ and pwd_ == db_password_:
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            show_pages('Main')

        else:
            messagebox.showerror('Login Status', 'invalid username or password')

    else:
        messagebox.showerror('', warn_)


class LoginFrame:
    def __init__(self, root):
        self.root = root

        master_ = tkinter.Frame(root, takefocus=7, padx=400, pady=200)
        master_.pack(fill=X)

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


        tkinter.Button(master_, text="Forgot Password", background='purple', font=f,

                       command=lambda: show_pages(page0='Forgot Password')
                       ).grid(row=9, column=1)

    def reset_pass(self): pass
