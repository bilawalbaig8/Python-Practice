arr = [	

{"name": "Hassan1", "id": 1},
{"name": "Hassan1", "id": 1},
{"name": "Hassan2", "id": 2},
{"name": "Hassan3", "id": 3},	
{"name": "Hassan4", "id": 4},
{"name": "Hassan5", "id": 5},

] 

#Need output {"hassan1":2, "hassan2":1 etc}

repeat = {}
#print(len(arr))

for i in arr:
	#print(i["name"])
	name = i["name"]
	#print(name)
	if name in repeat:
		repeat[name] += 1
	else:
		repeat[name] = 1

print(repeat)


'''
def abe(n):
	for i in range(0,n):
		print(i*5)

#abe(5)

def abc(n):
	for i in range(0,n):
		yield i*5

abc(5)
'''