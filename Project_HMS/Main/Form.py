import Classes
from tkinter import *
from tkinter import messagebox
import sys

pl = Classes.PatientList()

def addPatientform():

    def get_newpataientvalue():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_value.get()
        contactNo = contact_entry.get()
        condition = condition_entry.get()
        medicines = medicines_entry.get()
        remarks = remarks_entry.get()
        new_patient = Classes.Patient(name, age, gender, contactNo, condition, medicines, remarks)
        pl.add_patient(new_patient)
        print("Patient added successfully!")
        messagebox.showinfo("Success", "Patient added successfully!")

    def get_clearform():
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        gender_value.set(gender_values[0])
        contact_entry.delete(0, END)
        condition_entry.delete(0, END)
        medicines_entry.delete(0, END)
        remarks_entry.delete(0, END)

    canvas_root = Tk()
    canvas_root.geometry("800x1840")
    canvas_root.title("Patient Admission Form")
    canvas_root.resizable(False, False)

    header_frame = Frame(canvas_root, height=200, width=800, bg="#3b5998")
    header_frame.pack(side=TOP, fill=X)

    header = Label(header_frame, text="Patient Admission Form", font="Arial 24 bold", bg="#3b5998", fg="white")
    header.pack(pady=20)

    pdetail_frame = Frame(canvas_root, height=800, width=800, bg="silver", relief="solid", borderwidth=1)
    pdetail_frame.pack(side=TOP, fill="x", pady=20, padx=30)

    pdetail_header = Label(pdetail_frame, text="Personal Details", font="Arial 15 bold", bg="white", fg="#3b5998")
    pdetail_header.grid(row=0, column=0, columnspan=2, sticky="we", padx=100, pady=20)

    # configure the column widths
    pdetail_frame.columnconfigure(0, minsize=150)  # column 0 width
    pdetail_frame.columnconfigure(1, weight=1)    # column 1 width

    pdetail_text_padx = 20
    pdetail_text_pady = 8

    # Name
    name = Label(pdetail_frame, text="First Name: * ", anchor="w", font="Arial 12")
    name.grid(row=1, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    name_value = StringVar()
    name_entry = Entry(pdetail_frame, textvariable=name_value, font="Arial 12")
    name_entry.grid(row=1, column=1, sticky="w", ipady=3, ipadx=10)

    # Age

    age = Label(pdetail_frame, text="Age: * ", anchor="w", font="Arial 12")
    age.grid(row=3, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    age_value = StringVar()
    age_entry = Entry(pdetail_frame, textvariable=age_value, font="Arial 12")
    age_entry.grid(row=3, column=1, sticky="w", ipady=3, ipadx=10)

    # Gender

    gender = Label(pdetail_frame, text="Gender: * ", anchor="w", font="Arial 12")
    gender.grid(row=4, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    gender_values = ["Male", "Female", "Other"]
    gender_value = StringVar()
    gender_value.set(gender_values[0])  # Set default value
    gender_dropdown = OptionMenu(pdetail_frame, gender_value, *gender_values)
    gender_dropdown.config(font="Arial 12")
    gender_dropdown.grid(row=4, column=1,sticky="w")

    # Contact Number

    contact_no = Label(pdetail_frame, text="Contact No: * ", anchor="w", font="Arial 12")
    contact_no.grid(row=6, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    contact_value = StringVar()
    contact_entry = Entry(pdetail_frame, textvariable=contact_value, font="Arial 12")
    contact_entry.grid(row=6, column=1, sticky="w", ipady=3, ipadx=10)

    # condition

    condition = Label(pdetail_frame, text="condition:  ", anchor="w", font="Arial 12")
    condition.grid(row=7, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    condition_value = StringVar()
    condition_entry = Entry(pdetail_frame, textvariable=condition_value, font="Arial 12")
    condition_entry.grid(row=7, column=1, sticky="w", ipady=3, ipadx=10)

    # medicines

    medicines = Label(pdetail_frame, text="medicines:  ", anchor="w", font="Arial 12")
    medicines.grid(row=8, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    medicines_value = StringVar()
    medicines_entry = Entry(pdetail_frame, textvariable=medicines_value, font="Arial 12")
    medicines_entry.grid(row=8, column=1, sticky="w", ipady=3, ipadx=10)

    # remarks

    remarks = Label(pdetail_frame, text="remarks:  ", anchor="w", font="Arial 12")
    remarks.grid(row=9, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

    remarks_value = StringVar()
    remarks_entry = Entry(pdetail_frame, textvariable=remarks_value, font="Arial 12")
    remarks_entry.grid(row=9, column=1, sticky="w", ipady=3, ipadx=10)

    # Button Frame

    button_frame = Frame(canvas_root, height=800, width=800, bg="silver", relief="solid", borderwidth=1)
    button_frame.pack(fill="x", pady=20, padx=30)

    submitbutton = Button(button_frame, text="Submit", command = get_newpataientvalue)
    submitbutton.pack()


    cancelbutton = Button(button_frame, text="Cancel", command = get_clearform)
    cancelbutton.pack()

    canvas_root.mainloop()


def allrecords():
    def redirect_stdout(widget):
        def write(text):
            widget.insert(END, text)
            widget.see(END)

        sys.stdout.write = write

    # Function to print records to the redirected stdout
    def print_records():
        pl.view_directory()

    root = Tk()
    root.title("Console Output")

    text_widget = Text(root, wrap=WORD, font=("Helvetica", 12))
    text_widget.pack(expand=YES, fill=BOTH)

    redirect_stdout(text_widget)

    print_records()
    root.mainloop()
    pl.view_directory()

# Main Menu

canvas_root = Tk()
canvas_root.geometry("800x1840")
canvas_root.title("Patient Managment system")
canvas_root.resizable(False, False)

button_frame = Frame(canvas_root, height=800, width=800, bg="silver", relief="solid", borderwidth=1)
button_frame.pack(fill="x", pady=20, padx=30)

addrecord = Button(button_frame, text="Add Patient Record", command = addPatientform)
addrecord.pack()

search = Button(button_frame, text="Search Patient")
search.pack()

viewrecords = Button(button_frame, text="View all record", command = allrecords)
viewrecords.pack()

canvas_root.mainloop()
