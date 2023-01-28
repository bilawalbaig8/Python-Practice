wordOne = "alpepttleqeqdhdlphnbfdbjfgsfghhfgtdgtjhgb"
wordTwo = "apple"

dw1={}
dw2={}

for i in wordOne:
	try:
		dw1[i] = dw1[i] + 1
	except:
		dw1[i] = 1

print(dw1.items())  

for i in wordTwo:
	try:
		dw2[i] = dw2[i] + 1
	except:
		dw2[i] = 1

print(dw2.items())

extract=0
for i in dw2.keys():
	if i in dw1.keys() and dw2[i] <= dw1[i]:
		extract=extract+1
		#print(extract)

if extract == len(dw2.items()):
	print("it can be extracted")
else:
	print("it is not exists")
