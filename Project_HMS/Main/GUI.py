import tkinter as tk
from tkinter import messagebox
import Classes

# Function to handle button click event for adding a patient
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    contactNo = entry_contactNo.get()
    condition = entry_condition.get()
    medicines = entry_medicines.get()
    remarks = entry_remarks.get()
    new_patient = Classes.Patient(name, age, gender, contactNo, condition, medicines, remarks)
    pl.add_patient(new_patient)
    messagebox.showinfo("Success", "Patient added successfully!")
    clear_entries()

# Function to clear the entries in the add patient form
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_contactNo.delete(0, tk.END)
    entry_condition.delete(0, tk.END)
    entry_medicines.delete(0, tk.END)
    entry_remarks.delete(0, tk.END)

# Function to handle button click event for searching a patient
def search_patient():
    query = entry_search.get()
    found = pl.search_patient(query)
    if found:
        messagebox.showinfo("Success", "Patient found!")
    else:
        messagebox.showinfo("Not Found", "Patient not found.")

# Function to handle button click event for updating a patient
def update_patient():
    patient_name = entry_patient_name.get()
    pl.update_patient(patient_name)
    pl.search_patient(entry_search.get())

# Function to handle button click event for viewing all patients
def view_directory():
    pl.view_directory()

pl = Classes.PatientList()

# Create Tkinter window
root = tk.Tk()
root.title("Patient Management System")

# Create add patient button
button_add_patient = tk.Button(root, text="Add Patient", command=add_patient)
button_add_patient.grid(row=0, column=0, columnspan=2)

# Create search patient button
button_search_patient = tk.Button(root, text="Search", command=search_patient)
button_search_patient.grid(row=1, column=0, columnspan=2)

# Create view directory button
button_view_directory = tk.Button(root, text="View Directory", command=view_directory)
button_view_directory.grid(row=2, column=0, columnspan=2)

# #Create update patient form
# label_patient_name = tk.Label(root, text="Patient Name:")
# label_patient_name.grid(row=2, column=0)
# entry_patient_name = tk.Entry(root)
# entry_patient_name.grid(row=2, column=1)

# # Create labels and entries for the add patient form
# label_name = tk.Label(root, text="Name:")
# label_name.grid(row=0, column=0)
# entry_name = tk.Entry(root)
# entry_name.grid(row=0, column=1)
#
# label_age = tk.Label(root, text="Age:")
# label_age.grid(row=1, column=0)
# entry_age = tk.Entry(root)
# entry_age.grid(row=1, column=1)
#
# label_gender = tk.Label(root, text="Gender:")
# label_gender.grid(row=2, column=0)
# entry_gender = tk.Entry(root)
# entry_gender.grid(row=2, column=1)
#
# label_contactNo = tk.Label(root, text="Contact Number:")
# label_contactNo.grid(row=3, column=0)
# entry_contactNo = tk.Entry(root)
# entry_contactNo.grid(row=3, column=1)
#
# label_condition = tk.Label(root, text="Condition:")
# label_condition.grid(row=4, column=0)
# entry_condition = tk.Entry(root)
# entry_condition.grid(row=4, column=1)
#
# label_medicines = tk.Label(root, text="Medicines:")
# label_medicines.grid(row=5, column=0)
# entry_medicines = tk.Entry(root)
# entry_medicines.grid(row=5, column=1)
#
# label_remarks = tk.Label(root, text="Remarks:")
# label_remarks.grid(row=6, column=0)
# entry_remarks = tk.Entry(root)
# entry_remarks.grid(row=6, column=1)



# # Create search patient form
# label_search = tk.Label(root, text="Search Patient:")
# label_search.grid(row=0, column=0)
#
# entry_search = tk.Entry(root)
# entry_search.grid(row=0, column=1)





# #Create update patient button
# button_update_patient = tk.Button(root, text="Update Patient", command=update_patient)
# button_update_patient.grid(row=3, column=0, columnspan=2)


#Start Tkinter event loop

root.mainloop()