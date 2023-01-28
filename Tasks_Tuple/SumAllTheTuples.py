'''

Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]

'''

original_list = [(1, 2), (2, 3), (3, 4)]
original_list1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

result = []

# HardCoded Steps
# for i , x in original_list:
#     print(i+x)

for i in original_list1:
    result.append(sum(i))

print(result)