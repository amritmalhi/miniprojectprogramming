__author__ = 'BorisHunneman'


from tkinter.filedialog import *




img = "not"

def photo_upload_func():

    def printt():
        global img
        img = askopenfile(mode = 'r')
        print(img)

    def example():
        example_scrn = Tk()
        picture = Label(example_scrn, image=img)
        picture.pack()
    photo_upload = Tk()
    label = Label(photo_upload, text = "select picture please")
    button = Button(photo_upload, text = "Select", command = printt)
    button2 = Button(photo_upload, text = "Next", command = example)
    label.grid(row = 0, column = 0)
    button.grid(row = 0, column = 2)
    button2.grid(row = 1, column = 2)
    photo_upload.mainloop()

photo_upload_func()
