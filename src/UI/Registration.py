import tkinter
from tkinter import *
from tkinter import messagebox

from Db import Db


class Registration:

    def __init__(self, root):
        self.root = root
        right_frame = Frame(root, padx=300, pady=35)
        right_frame.pack(side='left', fill=X)

        right_frame.title = "Blueyes |Registration"

        f = ('Times', 14)

        conn = Db

        # widgets

        Label(right_frame,
              text="Enter Name",
              bg='#CCCCCC',
              font=f
              ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Email",
            bg='#CCCCCC',
            font=f
        ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Contact Number",
            bg='#CCCCCC',
            font=f
        ).grid(row=2, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Select Gender",
            bg='#CCCCCC',
            font=f
        ).grid(row=3, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Select Country",
            bg='#CCCCCC',
            font=f
        ).grid(row=4, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=5, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Re-Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=6, column=0, sticky=W, pady=10)

        gender_frame = LabelFrame(
            right_frame,
            bg='#CCCCCC',
            padx=10,
            pady=10,
        )

        register_name = Entry(
            right_frame,
            font=f
        )

        register_email = Entry(
            right_frame,
            font=f
        )

        register_mobile = Entry(
            right_frame,
            font=f
        )

        var = StringVar()
        var.set('male')

        countries = []
        variable = StringVar()
        world = open('countries.txt', 'r')
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[147])
        male_rb = Radiobutton(
            gender_frame,
            text='Male',
            bg='#CCCCCC',
            variable=var,
            value='male',
            font=('Times', 10),

        )

        female_rb = Radiobutton(
            gender_frame,
            text='Female',
            bg='#CCCCCC',
            variable=var,
            value='female',
            font=('Times', 10),

        )
        female_rb.pack()

        others_rb = Radiobutton(
            gender_frame,
            text='Others',
            bg='#CCCCCC',
            variable=var,
            value='others',
            font=('Times', 10)

        )
        others_rb.pack()

        register_country = OptionMenu(
            right_frame,
            variable,
            *countries)

        register_country.config(
            width=15,
            font=('Times', 12)
        )

        register_pwd = Entry(
            right_frame,
            font=f,
            show='*'
        )

        pwd_again = Entry(
            right_frame,
            font=f,
            show='*'
        )

        def insert_record():

            check_counter = 0
            warn_ = ""

            if register_name.get() == "":
                warn_ = "Name can't be empty"
            else:
                check_counter += 1

                if register_email.get() == "":
                    warn_ = "Email can't be empty"
                else:

                    check_counter += 1

                if register_mobile.get() == "":
                    warn_ = "Contact can't be empty"
                else:
                    check_counter += 1

                if var.get() == "":
                    warn_ = "Select Gender"
                else:
                    check_counter += 1

                if variable.get() == "":
                    warn_ = "Select Country"
                else:
                    check_counter += 1

                    if register_pwd.get() == "":
                        warn_ = "Password can't be empty"
                    else:
                        check_counter += 1

                    if pwd_again.get() == "":
                        warn_ = "Re-enter password can't be empty"
                    else:
                        check_counter += 1

                    if register_pwd.get() != pwd_again.get():
                        warn_ = "Passwords didn't match!"
                    else:
                        check_counter += 1

            if check_counter == 8:

                try:
                    conn.commit.__setattr__(
                        "INSERT INTO users VALUES (:name, :email, :contact, :gender, :country, :password)",
                        {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

                        })

                    conn.commit()
                    messagebox.showinfo('confirmation', 'Record Saved')

                except Exception as ep:

                    messagebox.showerror('Exception ', ep)
            else:
                messagebox.showerror('Error', warn_)

        register_btn = Button(
            right_frame,
            width=15,
            text='Register',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=insert_record
        )

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_country.grid(row=4, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)
        others_rb.pack(expand=True, side=LEFT)
