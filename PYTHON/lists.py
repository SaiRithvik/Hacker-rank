n = int(input())

list1=[]

for p in range(n):

	a = input()

	b = a.split(" ")

	if(b[0] == 'insert'):
		i = int(b[1])
		j = int(b[2])
		list1.insert(i,j)

	elif(b[0] == 'remove' ):
		k = int(b[1])
		list1.remove(k)

	elif(b[0] == 'append'):
		l = int(b[1])
		list1.append(l)

	elif(b[0] == 'sort'):
		list1.sort()

	elif(b[0] == 'print'):
		print(list1)

	elif(b[0] == 'pop'):
		list1.pop()

	elif(b[0] == 'reverse'):
		list1.reverse()









