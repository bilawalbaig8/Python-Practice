#Find the Prime Numbers
#value = 197
#factor = []

def primeNumber(value):
    factor = []
    for i in range(1, value+1):
        if value % i == 0:
            factor.append(i)

    print(factor)

    if len(factor) == 2:
        print("its a prime")
    else:
        print("its not a prime")

primeNumber(500)

