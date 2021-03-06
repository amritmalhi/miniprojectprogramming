__author__ = 'Avaritia'

from tkinter import *
import tkinter.messagebox as tm
from newsurface import Surface
import hashlib
import requests


class LoginFrame(Frame):

    """Constructor for the loginscreen"""
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Welcome to Photos.")
        self.label_2 = Label(self, text="Log in")
        self.label_3 = Label(self, text="Register")
        self.label_4 = Label(self, text="Username")
        self.label_5 = Label(self, text="Password")
        self.label_6 = Label(self, text="Username")
        self.label_7 = Label(self, text="Password")

        self.setup_window()


        self.pack()


    def setup_window(self):
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        self.entry_3 = Entry(self)
        self.entry_4 = Entry(self, show="*")

        self.button_1 = Button(self, text="Log in", command=self.login_button_clicked)
        self.button_2 = Button(self, text="Register", command=self.register_button_clicked)

        self.label_1.grid(row=0, column=0, columnspan=4, padx=200, pady=20)
        self.label_2.grid(row=1, column=0, columnspan=2, pady=5)
        self.label_3.grid(row=1, column=2, columnspan=2, pady=5)
        self.label_4.grid(row=2, column=0)
        self.label_5.grid(row=3, column=0)
        self.label_6.grid(row=2, column=2)
        self.label_7.grid(row=3, column=2)

        self.entry_1.grid(row=2, column=1)
        self.entry_2.grid(row=3, column=1)
        self.entry_3.grid(row=2, column=3)
        self.entry_4.grid(row=3, column=3)

        self.button_1.grid(row=4, column=0, columnspan=2, pady=5)
        self.button_2.grid(row=4, column=2, columnspan=2, pady=5)

    def clearall(self):
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
        self.entry_3.delete(0, 'end')
        self.entry_4.delete(0, 'end')

    def quit(self):
        self.root.destroy()

    def login_button_clicked(self):
        print("Clicked Button 1")
        username = self.entry_1.get()
        password = self.entry_2.get()
        print(username, password)
        n = hashlib.md5()
        n.update(password.encode('utf-8'))
        password = n.hexdigest()
        print(username, password)

        r = requests.post("http://davidlieffijn.nl/photos/login.php", data={'username':username, 'password':password})
        if r.text == 'true':
            print(username, "logged in")
            self.newWindow = Toplevel(self.master)
            self.app = Surface(self.newWindow, username)
            self.clearall()
        else:
            print("Unknown combination")
            tm.showerror("Login error", "Unknown combination")
            self.clearall()

    def register_button_clicked(self):
        print("Clicked Button 2")
        newusername = self.entry_3.get()
        password = self.entry_4.get()
        print(newusername, password)
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        password = m.hexdigest()
        print(newusername, password)
        if (len(newusername) > 3) and (len(password) > 3):
            r = requests.post('http://davidlieffijn.nl/photos/register.php', data={'username':newusername, 'password':password})
            print(r.text)
            if r.text == 'true':
                tm.showinfo("Registration", "A new account has been created for user " + newusername)
                self.clearall()
            else:
                tm.showerror("Registration", "Username already exists")
                self.clearall()
        else:
            print("Username or password not long enough")
            tm.showerror("Register error", "Username and password must be at least 4 characters long.")
            self.clearall()


def main():
    root = Tk()
    app = LoginFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()