'''

Consider a list (list = []). You can perform the following commands:

1: insert i e: Insert integer c at position i.
2: print: Print the list.
3: remove e: Delete the first occurrence of integer c.
4: append e: Insert integerc at the end of the list.
5: sort: Sort the list.
6: pop: Pop the last element from the list.
7: reverse: Reverse the list.

'''

# Mylist = []
#
# Mylist.insert(0, 5)
# Mylist.insert(1, 10)
# Mylist.insert(0, 6)
#
# print(Mylist)
#
from __future__ import print_function

if __name__ == '__main__':
    N = int(input())
    Mylist = []

    for i in range(N+1):

        Command = input().split()

        if Command[0] == "insert":
            Mylist.insert(int(Command[1]),int(Command[2]))
            # print(Mylist)

        elif Command[0] == "remove":
            Mylist.remove(int(Command[1]))

        elif Command[0] == "append":
            Mylist.append(int(Command[1]))

        elif Command[0] == "sort":
            Mylist.sort()

        elif Command[0] == "pop":
            Mylist.pop()

        elif Command[0] == "reverse":
            Mylist.reverse()

        elif Command[0] == "print":
            print(Mylist)
