n = int(input())

row = []

a = 0
b = 0
j = 0

for i in range(n):

	l = list(input().split())

	row.append(l)

for i in range(n):

		a = a + int(row[i][j])

		b = b + int(row[i][n-j-1])

		j = j + 1

if(a>b):
	print(a - b)
else:
	print(b - a)	


 