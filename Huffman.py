import heapq
from collections import defaultdict

codes = {}
freq = defaultdict(int)
minHeap = []

class MinHeapNode:
    def __init__(self, data, freq):
        self.left = None
        self.right = None
        self.data = data
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

def storeCodes(root, str):
    if root is None:
        return
    if root.data != '$':
        codes[root.data] = str
    storeCodes(root.left, str + "0")
    storeCodes(root.right, str + "1")


def HuffmanCodes():
    global minHeap
    for key in freq:
        minHeap.append(MinHeapNode(key, freq[key]))
    heapq.heapify(minHeap)
    while len(minHeap) != 1:
        left = heapq.heappop(minHeap)
        right = heapq.heappop(minHeap)
        top = MinHeapNode('$', left.freq + right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minHeap, top)
    storeCodes(minHeap[0], "")

def calcFreq(str, n):
    for i in range(n):
        freq[str[i]] += 1

def decode_file(root, s):
    ans = ""
    curr = root
    n = len(s)
    for i in range(n):
        if s[i] == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.left is None and curr.right is None:
            ans += curr.data
            curr = root
    return ans + '\0'

def Huffman_COING_FILE():
    tf = filedialog.askopenfilename(
        initialdir="/Users/Huffman/HF_DICT.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()

def Huffman_DECOING_FILE():
    tf = filedialog.askopenfilename(
        initialdir="/Users/Huffman/HF_DECODING.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()

def Huffman_FILE():
    tf = filedialog.askopenfilename(
        initialdir="/Users/Huffman/HF.txt",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf, "r")
    tf.close()


from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

with open ("/Users/TEXT_START.txt") as file:
    START=file.read()

def toFixed(numObj, digits=4):
    return f"{numObj:.{digits}}"

def makeHuffman(event):
    encodedString, decodedString= "", ""
    calcFreq(START, len(START))
    HuffmanCodes()
    HF_file_DICTS = open("/Users/Huffman/HF_DICT.txt", "w+")
    dictForHuffman = {i: START.count(i) for i in set(START)}
    HF_file_DICTS.write("Start dictionary:\n")
    HF_file_DICTS.write(str(dictForHuffman))
    HF_file_DICTS.write("\nDictionary after Huffman:\n")
    HF_file_DICTS.write(str(codes))
    HF_file_DICTS.close()

    for i in START:
        encodedString +=codes[i]

    HF_file = open("/Users/Huffman/HF.txt", "w+")
    for i in START:
        HF_file.write(encodedString)
    HF_file.close()

    decodedString = decode_file(minHeap[0], encodedString)
    HF_file_DECODING = open("/Users/Huffman/HF_DECODING.txt", "w+")
    HF_file_DECODING.write(decodedString)
    HF_file_DECODING.close()


    msg = Toplevel()
    msg.geometry(f'500x500')
    msg.title("HUFFMAN")
    msg.resizable(False, False)

    path = "/Users/images/w.png"
    image = Image.open(path)
    width = 2000
    ratio = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(ratio)))
    image = image.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(msg, width=width, height=height)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)


    btn_3 = Button(master=msg, text="HUFFMAN_CODS_FILE", borderwidth=0)
    btn_4 = Button(master=msg, text="HUFFMAN_DECODING_FILE", borderwidth=0)
    btn_5 = Button(master=msg, text="HUFFMAN_CODING_FILE", borderwidth=0)

    canvas.create_text(250,10, text="Result Huffman ",fill="Black", font="Verdana 12")

    btn_3.configure(command=Huffman_COING_FILE)
    btn_4.configure(command=Huffman_DECOING_FILE)
    btn_5.configure(command=Huffman_FILE)
    btn_3.place(x=150, y=250, width=225, height=40)
    btn_4.place(x=150, y=160, width=225, height=40)
    btn_5.place(x=150, y=80, width=225, height=40)

    btn = Button(master=msg, text="STOP")
    btn.configure(command=msg.destroy)
    btn.place(x=200, y=450, width=100, height=30)

    if (decodedString[:-1]==START) is True:
        batton = Button(master=msg, text="THE CONVERSION WAS SUCCESSFUL!", borderwidth=0)
        batton.configure(command=msg.destroy)
        batton.place(x=100, y=450, width=300, height=30)

    msg.mainloop()

