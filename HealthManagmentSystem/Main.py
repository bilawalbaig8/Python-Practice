import os


def getDate():
    import datetime
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %I:%M:%S %p")

    return date_time


def create_folder(file_name):
    if os.path.exists(file_name.lower()):
        print("{0} folder is exists".format(clientName))

    else:
        print("{0} folder is not exists".format(clientName))

        addFolder = input("Do you want to add this folder? (Y/N)")
        if addFolder.lower() == "y":
            os.mkdir(file_name)
            print("{0} folder is being created".format(clientName))

        else:
            print("Program is Quit")
            exit()


def create_file(file_name,type):
    entry = " "
    data = []

    while entry.lower() != "q" and entry.lower() != "quit":
        entry = input("Enter your {0} record or Enter (Q / Quit) to return \n".format(type))
        if entry.lower() in ['q', 'QUit']:
            break
        data.append(entry.capitalize())

    if os.path.exists(file_name):
        with open(file_name, "a") as f:
            for r in data:
                f.write(str(getDate()) + "\t" + str(r) + "\n")
    else:
        with open(file_name, "w") as f:
            for r in data:
                f.write(str(getDate()) + "\t" + str(r) + "\n")

    del data

    with open(file_name, "r") as f:
        record = f.read()
    print("\nAll the records")
    print(record)


if __name__ == "__main__":
    clientName = " "
    while clientName.lower() != "q" and clientName.lower() != "quit":

        clientName = input("Enter the name of client ")

        if clientName.lower() in ["q" , "QUit"]:
            break

        folderPath = os.path.join(os.getcwd(), clientName)
        create_folder(folderPath)

        entryChoice = int(input("\n Enter 1: To Record Diets "
                                "\n Enter 2: To Record Exercises "
                                "\n Enter 3: Back to Search "))

        if entryChoice == 1:
            dietFile = folderPath + "/" + clientName + "_Diet.txt"
            create_file(dietFile,"Diet")

        elif entryChoice == 2:
            excersiseFile = folderPath + "/" + clientName + "_excercise.txt"
            create_file(excersiseFile,"Excercise")

    print("exiting the program")
