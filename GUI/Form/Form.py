from tkinter import *

canvas_root = Tk()
canvas_root.geometry("800x300")

canvas_root.title("Admission Form")

canvas_header = Label(text="Admission Form" , font="Arial 18" )
canvas_header.pack()

name = Label(canvas_root, text="Username: ")
name.grid(row=0)

fathername = Label(canvas_root, text="Father's Name: ")
fathername.grid(row=1)

contact = Label(canvas_root, text="Contact Number: ")
contact.grid(row=2)





canvas_root.mainloop()