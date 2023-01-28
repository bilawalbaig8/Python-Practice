arr=[1,2,3,5,11,22,77,67,34,52,89]
odd=[]
even=[]
sumOfEven = 0
sumOfOdd = 0

for y in arr:
	#print(arr[y])
	if y % 2==1:
		odd.append(y)
		sumOfOdd += y
	if y % 2==0:
		even.append(y)
		sumOfEven += y

print(odd)
print(even)
print(sumOfOdd)
print(sumOfEven)