m = input()

a = list(input().split())

b = list(input().split())

for k in range(len(a)):

	a[k] = int(a[k])

for l in range(len(b)):

	b[l] = int(b[l])

a.sort()
b.sort()

c = a[len(a)-1]

d = b[0]



count = 0

for i in range(c , d + 1):

	if(len(a) > len(b)):

		for p in range(len(b)):
			if(b[p]%i == 0):
				if(i%a[p] == 0):
					for w in range(len(b),len(a)):
						if(i%a[w] == 0):
							if(p == len(b)-1 and w == len(a)-1):
								count = count + 1


	elif(len(b) > len(a)):

		for p in range(len(a)):
			if(i%a[p] == 0):
				if(b[p]%i == 0):
					for w in range(len(a),len(b)):
						if(b[w]%1 == 0):
							if(p == len(a)-1 and w == len(b)-1):
								count = count + 1

							
	else:
		for p in range(len(a)):
			if(i%a[p] == 0):
				if(b[p]%i == 0):
					if(p == len(a)-1):
						count = count + 1

print(int(count))							



		

	

		
