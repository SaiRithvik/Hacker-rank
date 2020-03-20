n = int(input())

record= {}

for i in range(n):
	
	a = input()

	b = list(a.split(" "))

	record[b[0]] = b[1]  +' ' + b[2] + ' ' + b[3]

c= input()

d = list(record[c].split(' '))

avg = 0

for j in range(len(d)):

	avg = avg + float(d[j])

avg = avg/len(d)	

print('%.1f'%avg)	



