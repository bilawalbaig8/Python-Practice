from tkinter import *

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

# First name
first_name = Label(pdetail_frame, text="First Name: * ", anchor="w", font="Arial 12")
first_name.grid(row=1, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

firstname_value = StringVar()
firstname_entry = Entry(pdetail_frame, textvariable=firstname_value, font="Arial 12")
firstname_entry.grid(row=1, column=1, sticky="w", ipady=3, ipadx=10)

# Last name

last_name = Label(pdetail_frame, text="Last Name: * ", anchor="w", font="Arial 12")
last_name.grid(row=2, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

lastname_value = StringVar()
lastname_entry = Entry(pdetail_frame, textvariable=lastname_value, font="Arial 12")
lastname_entry.grid(row=2, column=1, sticky="w",ipady=3, ipadx=10)

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

 # Blood Group

blood_group = Label(pdetail_frame, text="Blood Group: ", anchor="w", font="Arial 12")
blood_group.grid(row=5, column=0, sticky="w",padx=pdetail_text_padx, pady=pdetail_text_pady)


bloodgroup_values = ['NA', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
bloodgroup_value = StringVar()
bloodgroup_value.set(bloodgroup_values[0])  # Set default value
bloodgroup_dropdown = OptionMenu(pdetail_frame, bloodgroup_value, *bloodgroup_values)
bloodgroup_dropdown.config(font="Arial 12")
bloodgroup_dropdown.grid(row=5, column=1, sticky="w")


 # Contact Number

contact_no = Label(pdetail_frame, text="Contact No: * ", anchor="w", font="Arial 12")
contact_no.grid(row=6, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

contact_value = StringVar()
contact_entry = Entry(pdetail_frame, textvariable=contact_value, font="Arial 12")
contact_entry.grid(row=6, column=1, sticky="w", ipady=3, ipadx=10)

 # Email

email_address = Label(pdetail_frame, text="Email Address:  ", anchor="w", font="Arial 12")
email_address.grid(row=7, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

email_value = StringVar()
email_entry = Entry(pdetail_frame, textvariable=email_value, font="Arial 12")
email_entry.grid(row=7, column=1, sticky="w", ipady=3, ipadx=10)

 # Address

address = Label(pdetail_frame, text="Address:  ", anchor="w", font="Arial 12")
address.grid(row=8, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

address_value = StringVar()
address_entry = Entry(pdetail_frame, textvariable=address_value, font="Arial 12")
address_entry.grid(row=8, column=1, sticky="w", ipady=3, ipadx=10)

 # Payment

payment = Label(pdetail_frame, text="Paid: * ", anchor="w", font="Arial 12")
payment.grid(row=9, column=0, sticky="w", padx=pdetail_text_padx, pady=pdetail_text_pady)

payment_var = BooleanVar()
payment_checkbox = Checkbutton(pdetail_frame, text="Payment received?", variable=payment_var)
payment_checkbox.grid(row=9, column=1, sticky="w", ipady=3, ipadx=10)

canvas_root.mainloop()
