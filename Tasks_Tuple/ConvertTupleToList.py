'''

Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

'''

original_list = [(1, 2), (2, 3), (3, 4)]
original_list1 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

def tuplelist_to_list(list_values):
    converted_list = []
    for i in list_values:
        converted_list.append(list(i))

    print((converted_list))
    return converted_list


tuplelist_to_list(original_list)
tuplelist_to_list(original_list1)
