arr = ["LHR","MTN","ISB","FSD"]
position = 1
a = ["SGR"]

str = ""

# solution = 1

# # solution with slicing logic
# arr = arr[:position] + a + arr[position:]
# print(arr)

# solution = 2
# # solution with .insert logic
# for i in a:
#     str += i
#
# for i in range(len(arr)):
#     if i == position:
#         arr.insert(i,str)
#         break
# print(arr)

# solution = 3
# using append method

new_arr = []

for i in range(len(arr)):
    if i == position:
        new_arr.append(a[0])
    new_arr.append(arr[i])


arr = new_arr
print(arr)