import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageTk
import os

root = tk.Tk()

apps = []


def addFile():
    global im, size, width, entry
    file_name = filedialog.askopenfilename(
        initialdir="/ricecakeusa/", title='Select File', filetypes=(("jpg", "*.jpg"), ("All Files", "*.*")))
    im = Image.open(file_name)
    im.convert("RGBA")
    im = ImageOps.fit(im, (1280, 720))
    size = im.size
    width = int(size[0] / 2)
    label = tk.Label(root, text=file_name)
    label.place(relx=0.5, rely=0.53, anchor="s")

    entry = tk.Entry(root)
    entry.place(relx=0.5, rely=0.55, anchor="n")

    submit = tk.Button(root, text="Save As", padx=10, fg="black",
                       bg="white", command=addText)
    submit.place(relx=0.5, rely=0.68, anchor="s")


def addText():
    im_draw = ImageDraw.Draw(im, mode="RGBA")

    txt = entry.get()
    my_font = ImageFont.truetype(
        r"E:\ricecakeusa\assets\thumbnail-maker\hi_melody.ttf", int(width/3))
    w, h = im_draw.textsize(txt, font=my_font)
    xpoint = (size[0]-w)/2
    ypoint = (size[1]-h)/2
    im_draw.rectangle(
        [(0, ypoint-10), (size[0], ypoint+h+20)], fill="rgba(255, 114, 127, 255)")
    im_draw.text((xpoint, ypoint), txt,
                 font=my_font, stroke_width=int(width/200), stroke_fill="black")

    # put button on source image in position (0, 0)
    # im.paste(button_img, (int(width/2), int(height/2)))

    # save in new file
    file_location = filedialog.askdirectory(
        initialdir="/ricecakeusa/", title='Select Folder')
    file_name = file_location + "/" + txt + ".png"
    im.save(file_name, "PNG")
    im.show()


canvas = tk.Canvas(root, height=400, width=400, )
canvas.pack()

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#ff727f", command=addFile)
openFile.place(relx=0.5, rely=0.47, anchor="s")


root.mainloop()
