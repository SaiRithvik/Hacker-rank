x = int(input())

y = int(input())

z = int(input())

n = int(input())

print('[',end='')

for i in range(x + 1): 
		for j in range(y + 1):
			for k in range(z + 1):
				if(i + j + k != n):
					
					print([i,j,k],end='') 
					if(i != x or j!=y or k!=z):
						print(', ',end='')

print(']')						

	