#write a function to remove an item from the tuple

def to_remove(items_tuple , itemToRemove):
    """ we can use this function to remove any item from the tuple
        First variable is Tuple
        Second variable is Item to remove"""
        
    y = list(items_tuple)
    #print(y)
    remove = y.remove(itemToRemove)
    items_tuple = tuple(y)
    print(items_tuple)
    return items_tuple

fruit = ('apple', 'banana', 'mango', 'apple', 'banana')
itemToRemove = "mango"

to_remove(fruit , itemToRemove)