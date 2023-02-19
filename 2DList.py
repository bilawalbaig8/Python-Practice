'''

1- Find Average
2- Find Maximum
3- Find Minimum
4- Sort in ascending order
5- Sort in descending order

'''

m_list = [[12,13,14],[22,23,24],[32,33,34]]

def find_average(lst):
    sum = 0
    count = 0

    for row in lst:
        # print(row)
        for column in row:
            # print(column)
            sum = sum + column
            count = count + 1

    average = sum / count

    # return average
    print("\n Average : " , average)

def find_maximum(lst):
    maximum = lst[0][0]

    for row in lst:
        # print(row)
        for column in row:
            # print(column)
            if maximum < column:
                maximum = column
    # return maximum
    print("\n Maximum : " , maximum)

def find_minimum(lst):
    minimum = lst[0][0]

    for row in lst:
        # print(row)
        for column in row:
            # print(column)
            if minimum > column:
                minimum = column

    # return minimum
    print("\n Minimum : " , minimum)

def sort_accending_2dlst_as_1d(lst):
    oneDlist = []
    index = 0
    sorted_list = []

    for row in lst:
        # print(row)
        for column in row:
            oneDlist.append(column)

    # print(oneDlist)

    for i in range(len(oneDlist)):
        min = oneDlist[0]
        for j in range(len(oneDlist)):
            if min > oneDlist[j]:
                min = oneDlist[j]
                index = j
        sorted_list.append(min)
        oneDlist[index] = max(oneDlist)


    print("\n Sorted List accending order: ", sorted_list)


def sort_decending_2dlst_as_1d(lst):
    oneDlist = []
    index = 0
    sorted_list = []

    for row in lst:
        # print(row)
        for column in row:
            oneDlist.append(column)

    # print(oneDlist)

    for i in range(len(oneDlist)):
        max = oneDlist[0]
        for j in range(len(oneDlist)):
            if max < oneDlist[j]:
                max = oneDlist[j]
                index = j
        sorted_list.append(max)
        oneDlist[index] = min(oneDlist)


    print("\n Sorted List decending order: ", sorted_list)

def sort_decending_2dlst(lst):
    oneDlist = []
    index = 0
    sorted_list = []
    sorted2d_list = []

    for row in lst:
        # print(row)
        for column in row:
            oneDlist.append(column)

    # print(oneDlist)

    for i in range(len(oneDlist)):
        max = oneDlist[0]
        for j in range(len(oneDlist)):
            if max < oneDlist[j]:
                max = oneDlist[j]
                index = j
        sorted_list.append(max)
        oneDlist[index] = min(oneDlist)

    for i in range(0, len(sorted_list), 3):
        sorted2d_list.append(sorted_list[i:i + 3])

    print("\n Sorted list deccending order: ", sorted2d_list)


def sort_accending_2dlst(lst):
    oneDlist = []
    index = 0
    sorted_list = []
    sorted2d_list = []

    for row in lst:
        # print(row)
        for column in row:
            oneDlist.append(column)

    # print(oneDlist)

    for i in range(len(oneDlist)):
        min = oneDlist[0]
        for j in range(len(oneDlist)):
            if min > oneDlist[j]:
                min = oneDlist[j]
                index = j
        sorted_list.append(min)
        oneDlist[index] = max(oneDlist)

    for i in range(0, len(sorted_list), 3):
        sorted2d_list.append(sorted_list[i:i + 3])

    print("\n Sorted list accending order: ", sorted2d_list)


find_average(m_list)
find_maximum(m_list)
find_minimum(m_list)
sort_accending_2dlst_as_1d(m_list)
sort_accending_2dlst(m_list)
sort_decending_2dlst_as_1d(m_list)
sort_decending_2dlst(m_list)

