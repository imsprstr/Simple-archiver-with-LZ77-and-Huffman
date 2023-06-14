import Huffman
import LZ77

def callback(event):
    tf = filedialog.askopenfilename(
        initialdir="/Users/TEXT_START.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

window=Tk()
window.title("SIMPLE ARCHIVER")
window.geometry('500x500')
window.resizable(False,False)


path= "/Users/images/w.png"
image = Image.open(path)
width = 1000
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack(side="top", fill="both", expand="no")
canvas.create_image(0, 0, anchor="nw", image=image)

label = tk.Label(window, text='TEXT_START-start file',bg='#f5fafa')
canvas.create_window((110, 120), anchor="nw", window=label)
label.bind("<Button-1>", callback)


btn_1=tk.Label( master=window, text="LZ77",bg='#e4f6f7')
canvas.create_window((140, 180), anchor="nw", window=btn_1)
btn_1.bind("<Button-1>",LZ77.makeLZ77)


btn_2=Label(master=window,text="Huffman",bg='white')
canvas.create_window((250, 180), anchor="nw", window=btn_2)
btn_2.bind("<Button-1>",Huffman.makeHuffman)

buttonSTOP = Button(window,text='STOP', command=window.destroy, borderwidth=0)
buttonSTOP.place(x=200, y=450, width=50, height=30)

def openfile():
    tf = filedialog.askopenfilename(
        initialdir="/Users/TEXT_START.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf,"r")
    tf.close()


window.mainloop()

LZ77.makeLZ77()
Huffman.makeHuffman()
