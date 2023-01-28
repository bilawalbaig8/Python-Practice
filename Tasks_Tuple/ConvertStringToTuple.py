''' Write a Python program convert a given string list to a tuple.
 string: "python 3.0"
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0') '''

string = "python 3.0"
string_list = []

for i in string:
    string_list.append(i)

string_tuple = tuple(string_list)

print(string_tuple)