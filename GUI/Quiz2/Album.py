from tkinter import *


canvas_root = Tk()

canvas_root.geometry("700x400")

photo1 = PhotoImage(file="Photos/1.png")
scaled_image1 = photo1.subsample(10, 10)

photo2 = PhotoImage(file="Photos/2.png")
scaled_image2 = photo2.subsample(5, 5)

photo3 = PhotoImage(file="Photos/3.png")
scaled_image3 = photo3.subsample(10, 10)

photo4 = PhotoImage(file="Photos/4.png")
scaled_image4 = photo4.subsample(10, 10)

photo1_label = Label(image=scaled_image1)
photo1_label.pack()

photo2_label = Label(image=scaled_image2)
photo2_label.pack()

photo3_label = Label(image=scaled_image3)
photo3_label.pack()

photo4_label = Label(image=scaled_image4)
photo4_label.pack()


canvas_root.mainloop()