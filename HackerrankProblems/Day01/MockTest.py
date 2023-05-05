# n= 15
#
# for i in range(n+1):
#     if i % 3 ==0 and i % 5 == 0:
#         print ("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


arr1 = [1, 3, 3, 6, 7, 8, 9]
arr2 = [1, 2, 3, 4, 5, 6, 8, 9]


def median(arr):
    s = sorted(arr)
    l = len(arr)

    if l % 2 == 0:
        mid = l // 2
        return (s[mid - 1] + s[mid]) / 2
    else:
        mid = l // 2
        return s[mid]


print(median(arr1))
print(median(arr2))
