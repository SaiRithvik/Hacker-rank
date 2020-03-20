size_of_array=input()

a=input()

b=a.split()

p = 0
n = 0
z = 0
for i in range(int(size_of_array)):
	b[i]=int(b[i])
	if (b[i]>0):
		p+=1
	elif (b[i]<0):
		n+=1
	else:
		z+=1

print("%.6f"%(p/int(size_of_array)))
print("%.6f"%(n/int(size_of_array)))
print("%.6f"%(z/int(size_of_array)))