from File import *
def register():
    pId=input("Enter patient id")
    name=input("Enter patient name ")
    dob=input("Enter date of birth for patient(DD-MM-YYYY) ")
    address=input("Enter address of patient ")
    gender=input("Enter gender M or F ")
    contact=input("Enter contact number ")
    info=[]
    info.append(pId)
    info.append(name)
    info.append(contact)
    info.append(address)
    info.append(dob)
    info.append(gender)

    return info
def welcome():
    print("*************************************")
    print()
    print("### WELCOME TO PNY HOSPITAL PORTAL ###")
    print()
    print("**************************************")

if __name__=="__main__":
    welcome()
    file = "data.txt"
    #appendHeader(file)
    choice = int(input("Enter 1: To Register New Patient\nEnter 2: To View all the Patients "))

    if choice == 1:
        info = register()
        row = ''
        for r in range(len(info)):
            row = row+info[r]+'\t'
        appendRecord(file,row)

    elif choice==2:
        records=readAllRecords(file)
        print(records)

