# Write a Python program to find the index of an item of a tuple

fruit_Tuple = ('apple', 'banana', 'mango', 'apple', 'banana')


value_to_find = 'banana'

try:
    y = fruit_Tuple.index(value_to_find)
    print(" The given value is exists on index no : " + str(y))
except:
    print("not found")
