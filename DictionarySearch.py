dict1 = {
    "set":"The set() function creates a set object. The items in a set list are unordered, so it will appear in random order. Read more about sets in the chapter Python Sets.",

    "Operators":"In mathematics and computer programming, an operator is a character that represents a specific mathematical or logical action or process. For instance, 'x' is an arithmetic operator that indicates multiplication, while '&&' is a logical operator representing the logical AND function in programming.",

    "Tuples":"Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.",

    "Array":"What are Python Arrays? Arrays are a fundamental data structure, and an important part of most programming languages. In Python, they are containers which are able to store more than one item at the same time. Specifically, they are an ordered collection of elements with every value being of the same data type."
}

print("Hello, Please enter a 'Keyword'. You like to search")

# print("Please Enter")
# search = input()
while True:
    search = input("Please Enter : ")
    if search in dict1:
        print(dict1[search])
        print("<******End******>")
        secondInput = input("Do you like to check something else? Y/N : ")
        if secondInput == "Y":
            continue
        elif secondInput == "N":
            break
        else:
            print("input invalid")
            break
    else:
        print("input invalid")


# if search in dict1:
#     print(dict1[search])
#     print("<******End******>")
#
# else:
#     print("input invalid")

