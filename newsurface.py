__author__ = 'Avaritia'

from tkinter import *
import requests
from tkinter.filedialog import *
import json
import base64
from urllib.request import urlopen
import io
from PIL import Image, ImageTk


class Surface(Frame):
	username = ''

	def __init__(self, master, username):
		super().__init__(master)
		self.username = username
		pictures = self.loadImage()
		
		listbox = Listbox(self.master)
		listbox.grid(row = 1, rowspan = 6, column=0, columnspan=4)
		scrollbar = Scrollbar(listbox)
		scrollbar.grid(sticky=E, row = 0, rowspan = 6, column = 11, ipady = 1000)
		
		def upload():
			try:
				img = askopenfile(mode='rb')
				r = requests.post('http://www.davidlieffijn.nl/photos/upload.php',
				files={'submit': 'true', 'fileToUpload': img})
				print(r.text)
			except:
				print("No image selected")
		
		self.title_label = Label(self.master, text="Surface", font=("Helvetica", 20))
		self.title_label.grid(row=0, column=1, columnspan=2)

		self.upload_button = Button(self.master, text="Upload photo", command=upload)
		self.upload_button.grid(row=0, column=0, padx=50)

		self.welcome_label = Label(self.master, text="Welcome " + username)
		self.welcome_label.grid(row=0, column=3, padx=50)

		i = 1
		for picture in pictures:
			self.photo = Label(listbox, image=picture, height=400)
			self.photo.image = picture
			self.photo.grid(row=i, column=1, columnspan=2)
			print(i)
			i += 1




	def loadImage(self):
		r = requests.post('http://davidlieffijn.nl/photos/getphotos.php')
		data = json.loads(r.text)
		images = []
		for i in data:
			image_url = i['url']
			fd = urlopen(image_url)
			image_file = io.BytesIO(fd.read())
			image = Image.open(image_file)
			basewidth = 400
			wpercent = (basewidth/float(image.size[0]))
			hsize = int((float(image.size[1])*float(wpercent)))
			image = image.resize((basewidth, hsize), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(image)
			images.append(photo)
		return images
