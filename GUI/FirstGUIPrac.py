from tkinter import *

canvas_root = Tk()

canvas_root.geometry("733x434")

canvas_root.minsize(733,434)
canvas_root.maxsize(733,434)

canvas_root.title("Welcome To PyCharm")

canvas_header = Label(canvas_root, text="Welcome To PyCharm", font=('Arial', 18))
canvas_header.pack(padx=60,pady=60)


canvas_root.mainloop()
