arr = ["LHR","MTN","ISB","FSD"]
index = 1
a = "SGR"

for i in range(len(arr)):
    if i == index:
        arr.insert(i,a)
        break
print(arr)

# a1 = ["S","G","R"]
# b = ""
#
# for i in a1:
#     b += i
#
# for i in range(len(arr)):
#     if i == index:
#         arr.insert(i,b)
#         break
# print(arr)