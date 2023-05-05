import Classes

pl = Classes.PatientList()

print("====================================")
print("Welcome to Patient Management System")
print("====================================")

while True:
    print("\n1. Add Patient")
    print("2. Search Patient")
    print("3. View all the Patient Directory")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("Enter Patient Name : ")
        age = input("Enter Age : ")
        gender = input("Enter Gender (M/F/O) : ")
        contactNo = input("Enter Contact Number : ")
        condition = input("Enter Patient Condition : ")
        medicines = input("Enter Prescribed Medicines : ")
        remarks = input("Enter Remarks : ")
        new_patient = Classes.Patient(name, age, gender, contactNo, condition, medicines, remarks)
        pl.add_patient(new_patient)
        print("Patient added successfully!")

    elif choice == 2:

        query = input("Enter patient name or ID to search: ")
        found = pl.search_patient(query)

        if found:
            while True:
                patient_name = input("\nEnter patient name to update or 0 to exit: ")

                if patient_name == '0':
                    break

                pl.update_patient(patient_name)
                pl.search_patient(query)

    elif choice == 3:
        pl.view_directory()

    elif choice == 4:
        break
