"""

Assignment 1:
Console all the file data into a tabular format.

Assignment 2:
Add functionality to search a patient by his/her contact number

Assignment 3:
Convert the data from file into lists format
Write the data from lists to file again

Assignment 4:
Add delete and update record functionality
After Search by contact number

"""

from Functions import *


def register():
    pId = input("Enter patient id")
    name = input("Enter patient name ")
    dob = input("Enter date of birth for patient(DD-MM-YYYY) ")
    address = input("Enter address of patient ")
    gender = input("Enter gender M or F ")
    contact = input("Enter contact number ")
    info = []
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


if __name__ == "__main__":
    welcome()
    file = "data.txt"
    # appendHeader(file)
    choice = None

    while choice != 5:

        choice = int(input(
            " Enter 1: To Register New Patient\n "
            "Enter 2: To View all the Patients\n "
            "Enter 3: For Search\n "
            "Enter 4: To Update the Record\n "
            "Enter 5: For Quit "))

        if choice == 1:
            info = register()
            row = ''
            for r in range(len(info)):
                row = row + info[r] + '\t'
            appendRecord(file, row)

        # Console all the file data into a tabular format.

        elif choice == 2:
            records = readAllRecords(file)
            for i in range(len(records)):
                print(records[i])

        # If block for searching

        elif choice == 3 or 4:
            search = input("\nEnter 'Name or Contact Number' for search ")
            found = False
            records = readAllRecords(file)
            searchedRecord = []

            # Record Search Block
            for record_list in records:
                if search in record_list:
                    header = readHeader(file)
                    print("=====================================================================================")
                    print(header)
                    print(record_list, "\n \n")

                    # Saving list into Variable for later use
                    values = record_list.split("\t")
                    searchedRecord.append(values)
                    print(searchedRecord[0])

                    found = True
                    break

            if not found:
                print("\nResult not found")


            # Operations after search
            updateChoice = None

            while updateChoice != 4:
                updateChoice = int(input(
                                        " Enter 1: To add entry\n "
                                        "Enter 2: To update entry\n "
                                        "Enter 3: To delete the record\n "
                                        "Enter 4: Return to Main Menu\n "
                                        ))
                if updateChoice == 1:


                """
                elif updateChoice == 2:

                elif updateChoice == 3:

                elif updateChoice == 4:


                returnToMenu = input("\nDO you want to continue? (Y/N)")

                if returnToMenu != 'Y' and returnToMenu != 'y':
                    print("\nYou are in MainMenu")
                    break
                """

        elif choice == 5:
            print("Quit")

        subMenu = input("\nDO you want to continue? (Y/N)")

        if subMenu != 'Y' and subMenu != 'y':
            print("\nYou are quit")
            break

# # Convert Data into List
# file = "data.txt"
# record = readAllRecords(file)
# writenewfile("RecordList.txt", str(record))
