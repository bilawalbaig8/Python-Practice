from tkinter import *
from PIL import Image, ImageTk
import datetime

canvas_root = Tk()

canvas_root.geometry("1000x800")
canvas_root.title("NewPaper")


def every100(text):
    final_text = ''
    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text


news = []
photos = []

for i in range(0, 3):
    with open(f"News/News{i + 1}.txt") as f:
        text = f.read()
        news.append(every100(text))

        image = Image.open(f"News/Pic0{i + 1}.jpg")
        # TODO: resize images
        image = image.resize((255,255), Image.LANCZOS)
        photos.append(ImageTk.PhotoImage(image))

header = Frame(canvas_root, width=800, height=70)
Label(header, text="Latest News", font="lucida 33 bold").pack()

header.pack()

current_date = datetime.date.today()

date = Frame(canvas_root, width=100, height=50)
Label(date, text=str(current_date), font="lucida 13 bold").pack()
date.pack()

news01 = Frame(canvas_root, width=900, height=200)
Label(news01, text=news[0], justify='center', pady=10, padx=10).pack( side="left")
Label(news01 , image=photos[0], anchor="e").pack()
news01.pack(anchor="w")

news02 = Frame(canvas_root, width=900, height=200)
Label(news02 , image=photos[1], anchor="e").pack(side="left")
Label(news02, text=news[1], justify='center', pady=10, padx=10).pack()
news02.pack(anchor="w")

news03 = Frame(canvas_root, width=900, height=200)
Label(news03, text=news[2], justify='center', pady=10, padx=10).pack( side="left")
Label(news03 , image=photos[2], anchor="e").pack()
news03.pack(anchor="w")

canvas_root.mainloop()
