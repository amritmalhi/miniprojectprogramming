__author__ = 'Squarion'

from tkinter import *
from PIL import Image, ImageTk, ImageFilter

class Surface(Frame):
	def __init__(self, master):
		super().__init__(master)
		canvas = Canvas(self)
		frame = Frame(canvas)
		
		myscrollbar=Scrollbar(self,orient="vertical",command=canvas.yview)
		canvas.configure(yscrollcommand=myscrollbar.set)
		
		self.title_label = Label(self.master, text="Surface", font=("Helvetica", 20))
		self.title_label.pack()
		
		for i in range(0, 5, 1):
			image = Image.open("uther.png")
			out = image.filter(ImageFilter.SHARPEN)
			photo = ImageTk.PhotoImage(out)

			photo_label = Label(frame, image=photo, width="500")
			photo_label.image = photo # keep a reference!
			photo_label.pack()

			username_label = Label(frame, text="Geüpload door Harry")
			username_label.pack()
		
		myscrollbar.pack(side="right",fill="y")
		canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=600)
		canvas.pack(side="left")
		canvas.create_window((0,0),window=frame,anchor='nw')
		
		self.pack()
		
		#w, h = master.winfo_screenwidth(), master.winfo_screenheight()
		#master.overrideredirect(1)
		#master.geometry("%dx%d+0+0" % (w, h))

		'''self.title_label = Label(self.master, text="Surface", font=("Helvetica", 20))
		self.title_label.pack()
		

		canvas = Canvas(master, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
		canvas.grid(row=0, column=0, sticky=N+S+E+W)
		
		xscrollbar = Scrollbar(canvas, orient=HORIZONTAL)
		xscrollbar.grid(row=1, column=0, sticky=E+W)

		yscrollbar = Scrollbar(frame)
		yscrollbar.grid(row=0, column=1, sticky=N+S)
		

		for i in range(0, 5, 1):
			image = Image.open("uther.png")
			out = image.filter(ImageFilter.SHARPEN)
			photo = ImageTk.PhotoImage(out)

			photo_label_frame = LabelFrame(canvas)
			photo_label = Label(photo_label_frame, image=photo, width="500")
			photo_label.image = photo # keep a reference!
			photo_label.pack()

			#self.username_label = Label(self.master, text="Geüpload door Harry")
			#self.username_label.pack()
			canvas.create_window(0,0,window=photo_label, anchor="nw")

		

		xscrollbar.config(command=canvas.xview)
		yscrollbar.config(command=canvas.yview)
		self.button_1 = Button(self, text="Upload photo", command = self.upload_photo)
		#self.button_2 = Button(self, text="Register", command = self.register_button_clicked)


		self.button_1.pack()
		#self.button_2.grid(row=4, column=2, columnspan=2, pady=5)

		self.pack()'''
	
	def upload_photo(self):
		x = 3