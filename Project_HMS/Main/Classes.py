import pandas as pd
import openpyxl
from datetime import datetime


class Patient:

    def __init__(self, name, age, gender, contactNo, condition, medicines, remarks):
        self.id = 0
        self.name = name
        self.age = age
        self.gender = gender
        self.contactNo = contactNo
        self.condition = condition
        self.medicines = medicines
        self.remarks = remarks
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class PatientList:

    def __init__(self):
        self.Patient = {}

    def add_patient(self, patient):
        # read the last ID from the Excel sheet
        df = pd.read_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx")

        max_id = df["ID"].max()

        # assign a new ID based on the last ID
        patient.id = max_id + 1

        self.Patient[patient.id] = patient
        self.add_to_excel(patient)

    def add_to_excel(self, patient):
        df = pd.read_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx")
        new_patient_data = {'ID': patient.id, 'Date': patient.date, 'Patient Name': patient.name, 'Age': patient.age,
                            'Gender': patient.gender, 'Contact Number': patient.contactNo,
                            'Condition': patient.condition, 'Medicines': patient.medicines, 'Remarks': patient.remarks}
        df = pd.concat([df, pd.DataFrame(new_patient_data, index=[0])], ignore_index=True)
        df.to_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx", index=False)

    def view_directory(self):
        pd.options.display.width = 0  # Set the display width to 0 to display all columns in one line
        df = pd.read_excel(r"H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx")
        df = df.set_index('ID')
        pd.set_option('display.max_columns', None)
        print(df)

    def search_patient(self, query):
        found = False
        df = pd.read_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx")
        results = df[df['Patient Name'].str.contains(query, case=False)]
        if len(results) > 0:
            print(results.to_string(index=False))
            found = True
        else:
            print("Patient not found.")
            found = False

        return found

    def update_patient(self, query):
        df = pd.read_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx")
        patient_row = df.loc[df['Patient Name'] == query]
        if len(patient_row) > 0:
            condition = input("Enter new condition: ")
            medicines = input("Enter new medicines: ")
            remarks = input("Enter new remarks: ")
            df.loc[df['Patient Name'] == query, 'Condition'] = condition
            df.loc[df['Patient Name'] == query, 'Medicines'] = medicines
            df.loc[df['Patient Name'] == query, 'Remarks'] = remarks
            df.to_excel("H:\PythonAssignments\Project_HMS\DataBase\PatientRecord.xlsx", index=False)
            print("Patient record updated")