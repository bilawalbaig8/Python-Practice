"""
Output:
    AB
    CA
    AD
"""

s = 'AABCAAADA'
k = 3
n = len(s) // k
i = []
u = []

for j in range(0, len(s), k):
    i.append(s[j:j + k])

for j in range(len(i)):
    unique_set = ''.join(set(i[j]))
    u.append(unique_set)

print(u)
        # for y in x:
        #     print(y)
            # temp=[]
            # if y not in temp:
            #     temp.append(x)
            # print(temp)

