#write a function which will check the sentec of string by closing brackets

code = [" [ ( { { [ ( [ ] ) ] } } ) ]"]
code1 = [" [ ( ] }"]

stack = []
stack2 = []
for char in list(code[0]):
    if char in ["[" ,"(", "{"]:
        stack.append(char)
        #print(stack)

for char in reversed(list(code[0])):
    if char in ["}" ,")", "]"]:
        stack2.append(char)
        #print(stack)


print(stack)
print(stack2)


'''

    if char in ["(", "[", "{"]:
        stack.append(char)   


print(stack)
'''








'''
def is_valid_code(code):
    stack = []
    for char in code:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack:
                return False
            last_open = stack.pop()
            if (char == ")" and last_open != "(") or (char == "]" and last_open != "[") or (char == "}" and last_open != "{"):
                return False
    return not stack


code = "(this is [a valid] code message)"
if is_valid_code(code):
    print("The code is valid.")
else:
    print("The code is invalid.")

'''