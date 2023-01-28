# Write a python function. Which find repeated items in a tuple

def find_repeated_tuple(tup):

    """ this function is being used to find repeated values in a tuple"""
    
    repeated_item = []
    item_count = {}

    for i in tup:
        if i in item_count:
            item_count[i] += 1
        else:
            item_count[i] = 1

    #print(item_count.items())

    for key, values in item_count.items():
        #print(values)
        if values > 1:
            repeated_item.append(key)
        else:
            ("No repeatation Found")
    
    print(repeated_item)
    
        

fruit = ('apple', 'banana', 'mango', 'apple', 'banana')
find_repeated_tuple(fruit)


    
    

