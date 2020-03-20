n = int(input())

list1 = []

for i in range(n):

	a = input()
	b = float(input())

	list1.append([a,b])

print(list1)

minimum = list1[0][1]	
	
for j in list1:

	if(j[1]<minimum):
		minimum = j[1]

#print(minimum)	


count = 0

list3 = []

for k in range(n):
		if(list1[k][1] == minimum):

			list3.append(k)
			count = count + 1

print(list3)
#print(count)			
f = 0
for v in range(count):

	list1.remove(list1[list3[v]-f])
	f = f + 1
print(list1)

minimum = (list1[0][1])	
	
for t in range(len(list1)):

	

	if((list1[t][1])<minimum):
		minimum = (list1[t][1])

list2 = []

for g in list1:

	if(g[1] == minimum):
		list2.append(g[0])

list2.sort()

for s in range(len(list2)):
	print(list2[s])		

		

















		 







	