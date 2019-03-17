from tkinter import *
import tkinter.ttk as ttk
from EntryNum import EntryNum
from point import *
import re

# definicje zmiennych
root = Tk()
ttk.Style().theme_use('xpnative')

tile_size = 20
paczki = []  #Lista rozmiarow paczek

x = 0
y = 0

drawable_mode = True

def mouse_click(event):
    global drawable_mode
    if not drawable_mode:
        return

    x = event.x
    y = event.y

    width = entry_width.getNum()*tile_size
    height = entry_height.getNum()*tile_size
    if x > width:
        x = width
    if y > height:
        y = height
    x = round(x/tile_size)
    y = round(y/tile_size)

    if len(border_points)==0:
        point = Point(x, y)
        if valid_points(point):
            border_points.append(point)
            point.draw(canvas, tile_size)
    elif border_points[-1].x == x or border_points[-1].y == y:
        points = get_points(border_points[-1].x, border_points[-1].y, x, y)
        if valid_points(points):
            border_points.extend(points)
            for point in points:
                point.draw(canvas, tile_size)

    if len(border_points) > 1 and border_points[0].__eq__(border_points[-1]):
        draw_border()
        drawable_mode = False

def draw_border():
    for i in range(1, len(border_points)):
        canvas.create_line(border_points[i-1].x*tile_size, border_points[i-1].y*tile_size,
                           border_points[i].x*tile_size, border_points[i].y*tile_size)


def button_click():
    text = entry.get()
    listbox.insert(END, text)
    # paczki = re.split("; ", text)
    paczki = re.findall("[0-9], [0-9]", text)
    print(paczki)
    entry.delete(0, len(text))


def button_size_click():
    width = entry_width.getNum()
    height = entry_height.getNum()
    canvas.delete("all")
    canvas.create_rectangle(0, 0, width*tile_size, height*tile_size, outline="#fb0", fill="#fb0")

    for row in range(width):
        canvas.create_line(row*tile_size, 0, row*tile_size, height*tile_size, fill='#ccc')

    for col in range(height):
        canvas.create_line(0, col * tile_size, width * tile_size, col * tile_size, fill='#ccc')

    border_points.clear()


# RIGHT - wprowadzanie paczek

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, fill=Y)

rightUpFrame = Frame(rightFrame)
rightUpFrame.pack(side=TOP)

entry = ttk.Entry(rightUpFrame)
entry.pack(side=LEFT)

button = ttk.Button(rightUpFrame, text="DODAJ", command=button_click)
button.pack()

listbox = Listbox(rightFrame)
listbox.pack(side=LEFT, fill=Y)

# LEFT - magazyn

leftFrame = Frame(root)
leftFrame.pack(fill=BOTH, expand=YES)

leftUpFrame = Frame(leftFrame)
leftUpFrame.pack(side=TOP, fill=X)

label_width = Label(leftUpFrame, text='Width:')
label_width.pack(side=LEFT)
entry_width = EntryNum(leftUpFrame, text='30')
entry_width.pack(side=LEFT)

label_height = Label(leftUpFrame, text='Height:')
label_height.pack(side=LEFT)
entry_height = EntryNum(leftUpFrame, text='30')
entry_height.pack(side=LEFT)

button_size = ttk.Button(leftUpFrame, text="Apply", command=button_size_click)
button_size.pack(side=LEFT)

canvas = Canvas(leftFrame)
canvas.pack(side=BOTTOM, fill=BOTH, expand=YES)

canvas.bind("<Button-1>", mouse_click)

button_size_click()

root.mainloop()