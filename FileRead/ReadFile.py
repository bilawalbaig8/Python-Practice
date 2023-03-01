'''

Question 1:

Count the number of times these list of words occured
["Pakistan", "Jinnah", "India","England", "Muslim" , "Hindu"]
case insensitive match

Question 2:
Find the top 5 most occuring words with "Jinnah" ? After removing
buzzwords?


'''

def openFile(filename):
    file=open(filename,'r',encoding="utf8")
    data=file.read()
    return data

# Founding the list of words

file = openFile('Jinnah.txt')

words_to_find = ["Pakistan", "Jinnah", "India","England", "Muslim" , "Hindu"]

word_counts = {}

for word in words_to_find:
    word_counts[word] = file.lower().count(word.lower())

print(word_counts)
