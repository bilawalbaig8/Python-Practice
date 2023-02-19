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

    return average
    print("\n Average : " , average)

def find_maximum(lst):
    maximum = lst[0][0]

    for row in lst:
        # print(row)
        for column in row:
            # print(column)
            if maximum < column:
                maximum = column
    return maximum
    print("\n Maximum : " , maximum)

def find_minimum(lst):
    minimum = lst[0][0]

    for row in lst:
        # print(row)
        for column in row:
            # print(column)
            if minimum > column:
                minimum = column

    return minimum
    print("\n Minimum : " , minimum)

oneDlist = []
index = 0
sorted_list = []

for row in m_list:
    # print(row)
    for column in row:
        oneDlist.append(column)

# print(oneDlist)

for i in range(len(oneDlist)):
    min = [0]
    for j in range(len(oneDlist)):
        if min <= oneDlist[j]:
            min = oneDlist[j]
            index = j
        sorted_list.append(j)
        oneDlist[j] = min

print(sorted_list)





print(max,index)

# find_average(m_list)
# find_maximum(m_list)
# find_minimum(m_list)