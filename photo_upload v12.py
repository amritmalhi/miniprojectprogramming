__author__ = 'BorisHunneman'
import requests
from tkinter.filedialog import *

img = ""


def photo_upload_func():
    def printt():
        global img

        try:
            img = askopenfile(mode='rb')
            r = requests.post('http://www.davidlieffijn.nl/photos/upload.php',
                              files={'submit': 'true', 'fileToUpload': img})
            print(r.text)
        except:
            print("E")

    photo_upload = Tk()
    label = Label(photo_upload, text="select picture please")
    button = Button(photo_upload, text="Select", command=printt)
    label.grid(row=0, column=0)
    button.grid(row=0, column=2)
    photo_upload.mainloop()


photo_upload_func()