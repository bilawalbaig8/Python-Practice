'''string = "thisisnewstring"
can we remove the duplicate alfabet from the given string. ?'''

string = "thisisnewstring"

result = ""

for x in string:
	#print(x)
	if x not in result:
		print(x)
		result += x
		print(result)
		

print(result)