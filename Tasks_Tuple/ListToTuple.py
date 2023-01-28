def tuple_list(x):
    """ used append method to convert the tuple into list"""
    x_list = []
    for i in x:
        x_list.append(i)
    print(x_list)
    
def list_tuple(x):
    """ used casting to convert list in to tuple """
    y = tuple(x)
    print(y)


fruit_list = ['apple', 'banana', 'mango', 'apple', 'banana']
list_tuple(fruit_list)

fruit_Tuple = ('apple', 'banana', 'mango', 'apple', 'banana')
tuple_list(fruit_Tuple)