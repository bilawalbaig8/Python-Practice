'''

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Arjun
'''

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()


for name , scores in student_marks.items():
    if name == query_name:
        average = (sum(scores) / len(scores))
        print(name , "{:.2f}".format(round(average, 2)))
