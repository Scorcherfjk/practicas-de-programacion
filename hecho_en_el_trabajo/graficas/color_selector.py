"""Color Selector"""
from tkinter import *
from tkinter import colorchooser as ColorChooser

def hola():
	"""Devuelve el color seleccionado al Background de la interfaz"""
	rgb, html = ColorChooser.askcolor()
	print(html)
	root.config(bg=html)

root = Tk()
root.title("Primera Aplicacion")

color = Button(root,text="hola",command=hola)
color.pack()

root.mainloop()
