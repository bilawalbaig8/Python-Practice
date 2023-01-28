'''

Write a Python program to calculate the average value of the numbers in a given tuple of tuples

Original Tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

Average value of the numbers of the said tuple of tuples: [30.5, 34.25, 27.0, 23.25]

Original Tuple: ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

Average value of the numbers of the said tuple of tuples: [25.5, -18.0, 3.75]

'''


original_tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
original_tuple1 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

def average_tuple(tup):
    list1 = list(tup)
    average_list = []
    dict1 = {}
    for i in range(len(list1)):
        #print("=====")
        for x in list1[i]:
            average = sum(list1[i]) / len(list1[i])

        average_list.append(average)

    return average_list

print("Average value of the numbers of the said tuple of tuples: " + str(average_tuple(original_tuple)))

print("========================================")

print("Average value of the numbers of the said tuple of tuples: " + str(average_tuple(original_tuple1)))