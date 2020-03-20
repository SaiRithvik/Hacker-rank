n = int(input())

a = list(input().split())

maximum = int(a[0])

count = 0

for i in a:
	if(int(i) > maximum):
		maximum = int(i)

for j in a:
	if(int(j) == maximum):
		count = count + 1

print(count)		

