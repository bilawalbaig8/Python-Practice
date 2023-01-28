# convert tuple in to dictionary

def into_dict(item_Tuple):
    """This function will convert a tuple input into dictionary"""
    dict1 = {}
    for i in item_Tuple:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    item_Tuple = dict1

    print(item_Tuple)
    return item_Tuple

fruit = ('apple', 'banana', 'mango', 'apple', 'banana')
into_dict(fruit)