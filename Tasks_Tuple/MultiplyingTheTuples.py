'''

Write a Python program calculate the product, multiplying all the numbers of a given tuple
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648

'''
original_tuple = (4, 3, 2, 2, -1, 18)
original_tuple1 = (2, 4, 8, 8, 3, 2, 9)

def multiple_tuple(tup):
    product = 1

    for i in tup:
        product *= i

    print(product)
    return product


multiple_tuple(original_tuple1)