#string = "(hello  world"

def is_validate(string):
    stack = []
    pair = {"(" : ")" , "{" : "}" , "[" : "]"}
    result =  False
    noBrackets = 0

    for char in string:
        #print(char)
        if char in pair.keys():
            #print(char)
            stack.append(char)
            noBrackets += 1
        elif char in pair.values():
            #print(char)
            if not stack:
                result = False
                break
            last = stack.pop()
            if (char == ")" and last == "(" ) or (char == "}" and last == "{" ) or (char == "]" and last == "[" ):
                result = True
            else:
                result = False
                break

    #print(noBrackets)

    if result == True or noBrackets == 0:
        print ("correct")
    else:
        print ("incorrect")

is_validate("Hello World")
is_validate("(Hello World")
is_validate("[hello (world)]")
is_validate("[]hello (world)]}")
is_validate("[]hello (world){}[]{}")