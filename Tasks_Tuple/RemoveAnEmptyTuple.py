''' Write a Python program to remove an empty tuple(s) from a list of tuples
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] '''


sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

dict1 = {}

for i in sample_data:
    for x in i:
        if i in dict1:
            dict1[i] =+ 1
        else:
            dict1[i] = 1

sample_data.clear()
sample_data = list(dict1)

print(sample_data)
