n , m = input().split()

n = int(n)
m = int(m)

a = list(input().split())



for i in range(n):

	a[i] = int(a[i])


b = list(input().split())	

for i in range(m):

	b[i] = int(b[i])


a.sort()
b.sort()

c = max(a)

d = min(b)

count = 0
s = False

for i in range(c , d + 1):

	for k in range(n):

		if(i % a[k] == 0):

			if(k == n - 1):

				for l in range(m):

					if(b[l] % i ==0):

						if(l == m - 1):

							count = count + 1

						else:
							continue	

					else:

						s = True
						break
			else:
				continue			


				if(s == True):
					break


		else:
			break


print(count)





	





