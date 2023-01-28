#Print all the prime numbers
startRange = 2
endRange = 101
factor = []
primeNumbers = []

#print(value)

for i in range(startRange, endRange):
    for j in range(1,i+1):
        #print(i)
        if i % j == 0:
            factor.append(j)
    #print(str(i) + " => " + str(factor))
    if len(factor) == 2:
        primeNumbers.append(j)
    factor.clear()

print(primeNumbers)





'''
for i in range(len(value)):
    #print(value)
    if i >= 2:
        cal = i
        #print(cal)
        for y in range(2,cal):
            print(y)






for i in value:
    if value[i] % i == 0:
        factor.append(i)

    if len(factor) == 2:
        primeNumbers.append(i)

print(primeNumbers)


for i in range(0, 100):
    if value % i == 0:
        factor.append(i)

print(factor)

if len(factor) == 2:
    print("its a prime")
else:
    print("its not a prime")
'''