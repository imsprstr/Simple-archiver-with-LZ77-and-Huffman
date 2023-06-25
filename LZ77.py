def lz77_coding(uncompressed):
    window_size = 256
    lookahead_buffer_size = 64
    compressed = []
    i = 0
    while i < len(uncompressed):
        match_found = False
        best_match_distance = window_size
        best_match_length = 0
        window_start = max(0, i - window_size)
        lookahead_buffer_end = min(i + lookahead_buffer_size, len(uncompressed))
        for j in range(i + 1, lookahead_buffer_end + 1):
            current_window = uncompressed[window_start:i]
            current_search = uncompressed[i:j]
            if current_search in current_window:
                match_found = True
                match_distance = i - window_start - current_window.index(current_search)
                match_length = len(current_search)
                if match_length > best_match_length:
                    best_match_distance = match_distance
                    best_match_length = match_length
        if match_found:
            compressed.append((best_match_distance, best_match_length,uncompressed[i]))
            i += best_match_length
        else:
            compressed.append((0,0, uncompressed[i]))
            i += 1
    return compressed


def lz77_decoding(compressed):
    uncompressed = []
    for item in compressed:
        if item[0] == 0 or item[1]==0:
            uncompressed.append(item[2])
        else:
            start = len(uncompressed) - item[0]
            for i in range(item[1]):
                uncompressed.append(uncompressed[start + i])
    return ''.join(uncompressed)

def LZ77_COING_FILE():
    tf = filedialog.askopenfilename(
        initialdir="/Users/LZ77/LZ77_CODING_comp.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()


def LZ77_DECODING_FILE():
    tf = filedialog.askopenfilename(
        initialdir="/Users/LZ77/LZ77_DECODING_decomp.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()

with open ("/Users/TEXT_START.txt") as file:
    START=file.read()

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


def writeFile(path,stringWr):
    write_file = open(path, "w+")
    write_file.write(stringWr)
    write_file.close()
    
def makeLZ77(event):
    msg = Toplevel()
    msg.geometry('500x500')
    msg.title("LZ77")
    msg.resizable(False, False)

    path = "/Users/images/w.png"
    image = Image.open(path)
    width = 1600
    ratio = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(ratio)))
    image = image.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(msg, width=width, height=height)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    btn_3 = Button(master=msg, text="LZ77_CODING_FILE", borderwidth=0)
    btn_4 = Button(master=msg, text="LZ77_DECODING_FILE", borderwidth=0)

    writeFile("/Users/LZ77/LZ77_CODING_comp.txt", str(lz77_coding(START)))
    writeFle("/Users/LZ77/LZ77_DECODING_decomp.txt", str(lz77_decoding(lz77_coding(START))))

    canvas.create_text(250,50,text="Result LZ77", fill="Black", font="Verdana 12")

    btn_3.configure(command=LZ77_COING_FILE)
    btn_4.configure(command=LZ77_DECODING_FILE)
    btn_3.place(x=150, y=250, width=225, height=40)
    btn_4.place(x=150, y=100, width=225, height=40)

    btn = Button(master=msg, text="STOP")
    btn.configure(command=msg.destroy)
    btn.place(x=200, y=450, width=100, height=30)


    if (lz77_decoding(lz77_coding(START)) == START) is True:
        batton=Button(master=msg, text="THE CONVERSION WAS SUCCESSFUL!", borderwidth=0)
        batton.configure(command=msg.destroy)
        batton.place(x=100, y=450, width=300, height=30)

    msg.mainloop()
