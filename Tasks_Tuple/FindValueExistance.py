# Write a Function to check whether an element exists within a tuple

def if_exists(item_tuple , check_value):
    """ You can find the existance of an item in the tuple
    
    First Variable is Tuple
    Second Variable is value to find
    
    """
      
    found = "Not Found"
    for i in item_tuple:
        if i == check_value:
            found = "Found"
            break

    print(found)

fruit = ('apple', 'banana', 'mango', 'apple', 'banana')
check_value = "Kiwi"
if_exists(fruit , check_value)

fruit = (0, 1, 5, 2, 6, 87, 4)
check_value = 8
if_exists(fruit , check_value)