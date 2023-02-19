marks = [45,51,32,34,22,30,31]
max = marks[0]
min = marks[0]

for i in range(len(marks)):
    if max < marks[i]:
        max=marks[i]
    elif min > marks[i]:
        min=marks[i]

print(max,min)