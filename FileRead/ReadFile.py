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

def removebuzzwords(data):
    buzzwords = ["as","if","the","was","in","off","of","this","a","at","had","and","also","is"]
    impwords = []
    for word in data.split(" "):
        if word.lower() not in buzzwords:
            impwords.append(word.lower())

    return impwords

file = openFile('Jinnah.txt')


# buzzword remove

without_buzzwords = removebuzzwords(file)
# print(without_buzzwords)

# Founding the list of words


lowercased_document = file.lower().split()

words_to_find = ["Pakistan", "Jinnah", "India","England", "Muslim" , "Hindu"]

word_counts = {}

for word in words_to_find:
    lowercased_word = word.lower()
    if lowercased_word in lowercased_document:
        word_counts[word] = lowercased_document.count(lowercased_word)
    else:
        word_counts[word] = 1

print(word_counts)


# 5 most recurring words with "Jinnah"

words_to_find = "Jinnah"

#collecting previous words
word_collect = []
recurring_word_count = {}

previous_word = ''

for word in without_buzzwords:
    if word == words_to_find.lower():
        word_collect.append(previous_word)
    else:
        previous_word = word

# print(word_collect)

# counting the recurring words

for count in word_collect:
    if count in recurring_word_count:
        recurring_word_count[count] += 1
    else:
        recurring_word_count[count] = 1

print(recurring_word_count)


# counting Maximum recurring words
