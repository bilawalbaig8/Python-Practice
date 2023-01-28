print("This calculator will help you to perform some basic arithmatic operations")
print("Following operations can be select")
print("+ for addition")
print("- for subtraction")
print("* for Multiply")
print("// for division whole value")
print("/ for division decimal value")
print("** for power")
print("% for reminder")


initialize = True

while initialize:
    operator = input("Enter your Operator : ")
    a = input("Enter first value : ")
    b = input("Enter second value : ")
    if operator == "+":
        r = int(a)+int(b)
        print(str(a) + " + " + str(b) + " = " + str(r))
    elif operator == "-":
        r = int(a) - int(b)
        print(str(a) + " - " + str(b) + " = " + str(r))
    elif operator == "*":
        r = int(a) * int(b)
        print(str(a) + " * " + str(b) + " = " + str(r))
    elif operator == "/":
        r = int(a) / int(b)
        print(str(a) + " / " + str(b) + " = " + str(r))
    elif operator == "//":
        r = int(a) // int(b)
        print(str(a) + " // " + str(b) + " = " + str(r))
    elif operator == "**":
        r = int(a) ** int(b)
        print(str(a) + " power " + str(b) + " = " + str(r))
    elif operator == "%":
        r = int(a) % int(b)
        print(str(a) + " % " + str(b) + " = " + str(r))
    else:
        print("invalid input")
    i = input("Do you like to try again Y/N : ")
    if i == "Y":
        continue
    elif i == "N":
        break
    else:
        print("invalid")
        break