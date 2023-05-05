# find Unique
a = [1,2,3,4,3,2,1]

count = {}

for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for key, value in count.items():
    if value == 1:
        print(key)
