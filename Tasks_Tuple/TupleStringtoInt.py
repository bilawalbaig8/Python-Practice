'''
Write a Python program to convert a tuple of string values to a tuple of integer values.
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))
'''


original_tuple_values = (('333', '33'), ('1416', '55'))
list1 = []
new_tuple_values = ()

tuple_list = list(original_tuple_values)
#print(tuple_list)

for i in range(len(tuple_list)):
    inner_list = []
    #print("====")
    for x in tuple_list[i]:
        inner_list.append(int(x))
        #print(inner_list)
    list1.append(tuple(inner_list))

#print(list1)
new_tuple_values = tuple(list1)

print(new_tuple_values)
