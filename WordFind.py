wordOne = "alpepttleqeqad"
wordTwo = "apple"
testing = "hi"
extractedWord= ""

for x in wordTwo:
  #print(x)
  if x in wordOne:
    extractedWord += x

# Debuging 
    print(extractedWord)
    #print(x)


print(extractedWord)

if wordTwo == extractedWord:
  print("Matched")

else:
  print("NotMatched")