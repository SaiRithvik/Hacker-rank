a = list(input().split())

k1 = []
k2 = []

k1.append(a[0])
k1.append(a[1]) 

k2.append(a[2])
k2.append(a[3])

for j in range(k1[1]):

	if(((k2[0] - k1[0]) + j*k2[1])%k1[1] == 0):
		print('YES')
	else:
		print('NO')
		






