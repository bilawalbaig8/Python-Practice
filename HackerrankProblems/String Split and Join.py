# a = "this is a string  "
#
# b = a.strip()
#
# print(b)
#
#
# splita = b.split(" ")
#
# print (splita)
#
# splitjoin = ("_").join(splita)
#
# print(splitjoin)


def split_and_join(line):
    line = line.strip()
    splitline = line.split(" ")
    joinline = ("_").join(splitline)


    return joinline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)