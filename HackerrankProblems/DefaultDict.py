from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print (i)
#


# code for taking input
n, m = map(int, input().split())
groupA = []
groupB = []


for i in range(n):
    A = input().strip()
    groupA.append(A)

for j in range(m):
    B = input().strip()
    groupB.append(B)
#
# print(groupA)
# print(groupB)



#
# A = ['a', 'a', 'b', 'a', 'b']
# B = ['a', 'b','c']
notfound = -1

for i in range(len(groupB)):
    check = True
    found = False
    while check:
        for j in range(len(groupA)):
            if groupA[j] == groupB[i]:
                print(j + 1, end=' ')
                found = True
        check = False
    if not found:
        print(notfound, end=' ')
    print()



# for i in groupB:
#     if i in d.keys():
#
#     else:
#         print("not found")

# for i in range(len(groupB)):
#     check = True
#     while check:
#         for j in range(len(groupA)):
#             if groupA[j] in groupB[i]:
#                 print(j + 1)
#             else:
#                 print(- 1)
#                 check = False


# code as per hackerrank inputs

from collections import defaultdict

# # n, m = map(int, input().split())
# A = list(input().split('\n'))
# B = list(input().split('\n'))




# notfound = -1
#
# # Remove any empty strings from the lists
# A = list(filter(None, A))
# B = list(filter(None, B))
#
# # Create a dictionary to store the indices of each element in A
# index_dict = defaultdict(list)
# for i in range(len(A)):
#     index_dict[A[i]].append(i + 1)
#
# for i in range(len(B)):
#     found_indices = index_dict[B[i]] if B[i] in index_dict else []
#     if len(found_indices) > 0:
#         print(" ".join(str(idx) for idx in found_indices))
#     else:
#         print(notfound)

