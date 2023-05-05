# diagnol differece
a = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

# a = [
#     [6, 6, 7, -10, 9, -3, 8, 9, -1],
#     [9, 7, -10, 6, 4, 1, 6, 1, 1],
#     [-1, -2, 4, -6, 1, -4, -6, 3, 9],
#     [-8, 7, 6, -1, -6, -6, 6, -7, 2],
#     [-10, -4, 9, 1, -7, 8, -5, 3, -5],
#     [-8, -3, -4, 2, -3, 7, -5, 1, -5],
#     [-2, -7, -4, 8, 3, -1, 8, 2, 3],
#     [-3, 4, 6, -7, -7, -8, -3, 9, -6],
#     [-2, 0, 5, 4, 4, 4, -3, 3, 0]
#     ]


left_diagonal = []
right_diagonal = []

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            left_diagonal.append(a[i][j])

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            reverse = len(a[i]) - j - 1
            right_diagonal.append(a[i][reverse])

print(left_diagonal)
print(right_diagonal)

difference = abs((sum(left_diagonal)) - (sum(right_diagonal)) * 1)

print(difference)
