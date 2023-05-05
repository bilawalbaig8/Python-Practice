#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def miniMaxSum(arr):
#     # Write your code here
#
# if __name__ == '__main__':
#
#     arr = list(map(int, input().rstrip().split()))
#
#     miniMaxSum(arr)








arr = [1,2,3,4,5]
templist = []
sumlist = []


for i in range(len(arr)):
    templist = arr.copy()
    templist.pop(i)
    sumlist.append(sum(templist))

print(f"Minimum value: {min(sumlist)}, Maximum value: {max(sumlist)}")
