'''

Write a Python program to check if a specified element presents in a tuple of tuples.
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White present in said tuple of tuples!
True
Check if Olive present in said tuple of tuples!
False

'''

original_list = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
value_to_check = 'Olive'
found = True

for i in original_list:
    for x in i:
        if value_to_check == x:
            found = True

            break
        else:
            found = False

    break

print(found)

