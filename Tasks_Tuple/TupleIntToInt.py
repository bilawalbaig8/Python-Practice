'''

Write a Python program to convert a given tuple of positive integers into an integer.
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570

'''

original_tuple = (1, 2, 3)
original_tuple1 = (10, 20, 40, 5, 70)

def tuple_int(tup):
    string = ''
    result = 0


    for i in tup:
        string += str(i)

    result = int(string)
    #print(result)
    return result

print(tuple_int(original_tuple))
print(tuple_int(original_tuple1))
