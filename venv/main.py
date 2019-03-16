from tkinter import *
import tkinter.ttk as ttk
from EntryNum import EntryNum

root = Tk()
ttk.Style().theme_use('xpnative')

tile_size = 20

# RIGHT

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, fill=Y)

rightUpFrame = Frame(rightFrame)
rightUpFrame.pack(side=TOP)

entry = ttk.Entry(rightUpFrame)
entry.pack(side=LEFT)

def button_click():
    text = entry.get()
    listbox.insert(END, text)
    entry.delete(0, len(text))

button = ttk.Button(rightUpFrame, text="DODAJ", command=button_click)
button.pack()

listbox = Listbox(rightFrame)
listbox.pack(side=LEFT, fill=Y)

# LEFT

leftFrame = Frame(root)
leftFrame.pack(fill=BOTH, expand=YES)

leftUpFrame = Frame(leftFrame)
leftUpFrame.pack(side=TOP, fill=X)

label_width = Label(leftUpFrame, text='Width:')
label_width.pack(side=LEFT)
entry_width = EntryNum(leftUpFrame, text='10')
entry_width.pack(side=LEFT)

label_height = Label(leftUpFrame, text='Height:')
label_height.pack(side=LEFT)
entry_height = EntryNum(leftUpFrame, text='10')
entry_height.pack(side=LEFT)

def button_size_click():
    width = entry_width.getNum()
    height = entry_height.getNum()
    canvas.delete("all")
    canvas.create_rectangle(0, 0, width*tile_size, height*tile_size, outline="#fb0", fill="#fb0")

    for row in range(width):
        canvas.create_line(row*tile_size, 0, row*tile_size, height*tile_size)

    for col in range(height):
        canvas.create_line(0, col * tile_size, width * tile_size, col * tile_size)


button_size = ttk.Button(leftUpFrame, text="Apply", command=button_size_click)
button_size.pack(side=LEFT)

canvas = Canvas(leftFrame)
canvas.pack(side=BOTTOM, fill=BOTH, expand=YES)

button_size_click()

root.mainloop()