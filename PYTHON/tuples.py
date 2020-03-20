n = int(input())

a = input()

b = a.split(" ")

t = tuple(b)

if(len(b)<=n):

	for i in range(n):
		b[i] = int(b[i])

	t= tuple(b)	

	print(hash(t))	