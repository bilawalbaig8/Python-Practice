rows = int(input("enter number of rows:"))
style = int(input("1 or 0:"))

if style == True:
    for i in range(rows):
        for j in range(i+1):
            print("*", end="")
        print()

elif style == False:
    for i in range(rows):
        for j in range(i,rows):
            print("*", end="")
        print()

