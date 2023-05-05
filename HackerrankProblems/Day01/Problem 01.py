arr = [-4, 3, -9, 0, 4, 1]
negative = []
positive = []
zero = []

for i in arr:
    # print(i)
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
    elif i == 0:
        zero.append(i)

negative_value = len(negative)/len(arr)
positive_value = len(positive)/len(arr)
zero_value = len(zero)/len(arr)
print("{:.6f}".format(negative_value))
print("{:.6f}".format(positive_value))
print("{:.6f}".format(zero_value))