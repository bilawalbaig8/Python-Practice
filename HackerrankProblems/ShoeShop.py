'''

inputs

total shoes = x = 10
shoes acording to sizes = 2 3 4 5 6 8 7 6 5 18
TOtal customers = n = 6
Customer 1 = shoessize : 6 , shoes price : 55
Customer 2 = shoessize : 6 , shoes price : 45
Customer 3 = shoessize : 6 , shoes price : 55
Customer 4 = shoessize : 4 , shoes price : 40
Customer 5 = shoessize : 18 , shoes price : 60
Customer 6 = shoessize : 10 , shoes price : 50

Print how much you earn

'''

from collections import Counter

x = 10
shoessizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
n = 6
customers = [[6, 55],
             [6, 45],
             [6, 55],
             [4, 40],
             [18, 60],
             [10, 50],
             ]
pricecollected = []

inventorycount = (Counter(shoessizes))
print(inventorycount)

for i in customers:
    size = i[0]
    price = i[1]

    for key, values in inventorycount.items():
        if key == size:
            if inventorycount[key] > 0:
                inventorycount[key] -= 1
                pricecollected.append(price)

print(sum(pricecollected))

# as per HackerRank Requirement

# from collections import Counter

# X = int(input())
# ShoeSizes = list(map(int, input().split()))
# N = int(input())
# sales = []
# pricecollected = []
# inventorycount = (Counter(ShoeSizes))
#
# for i in range(N):
#     for line in input().split('\n'):
#         if line.strip():  # Check if line is not empty
#             x, y = map(int, line.strip().split())
#             sales.append((x, y))
#
# for i in sales:
#     size = i[0]
#     price = i[1]
#
#     for key, values in inventorycount.items():
#         if key == size:
#             if inventorycount[key] > 0:
#                 inventorycount[key] -= 1
#                 pricecollected.append(price)
#
# print(sum(pricecollected))
