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
    choice = int(input(" Enter 1: To Register New Patient\n Enter 2: To View all the Patients\n Enter 3: For Search "))

    if choice == 1:
        info = register()
        row = ''
        for r in range(len(info)):
            row = row+info[r]+'\t'
        appendRecord(file,row)

    # Console all the file data into a tabular format.

    elif choice==2:
        records = readAllRecords(file)
        for i in range(len(records)):
            print(records[i])

    elif choice==3:
        search = input("Enter 'Name or Contact Number' for search ")
        found = False
        records = readAllRecords(file)
        for record_list in records:
            if search in record_list:
                print(record_list)
                found = True
                break

        if not found:
                print("Result not found")



