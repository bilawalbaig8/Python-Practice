# name = "Harry"
# score = 37.21
'''
Inputs

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


'''

result = []
scores = []

for n in range(int(input())):
    name = input()
    score = float(input())
    result.append([name, score])
    if score not in scores:
        scores.append(score)



# print(result)
sorted_list = sorted(scores)
secondlowest = sorted_list
# print(sorted_list)




# ''' Not an optimized code'''
# # Some variables
# grade_dict = {}
# orignal_score_lst = []
# modified_score = []
# low_score_student = []
#
# # Saving the input in dictionary and Score in the list as well
# for n in range(int(input())):
#     name = input()
#     score = float(input())
#
#     grade_dict[name] = score
#     orignal_score_lst.append(score)
#
# # Sorting the score list
# for i in orignal_score_lst:
#     if i not in modified_score:
#         modified_score.append(i)
#
# sorted_list = sorted(modified_score)
#
# # finding the name of student who has second minimum score
# second_minimum_score = sorted_list[1]
#
# for name, score in grade_dict.items():
#     if score == second_minimum_score:
#         low_score_student.append(name)
#
# # Sorting and printing the name in order
# sorted_name = sorted(low_score_student)
# # print(sorted_name)
#
# for i in sorted_name:
#     print(str(i))
#
