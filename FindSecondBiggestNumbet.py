original_set = [3, 5, 7, 7, 6, 2]

new_list = []

for i in original_set:
    if i not in new_list:
        new_list.append(i)

sorted_list = sorted(new_list, reverse=True)

print(sorted_list[1])
