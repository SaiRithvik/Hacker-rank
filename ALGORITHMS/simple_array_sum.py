len_list=input("enter list size")

a=input("enter elements with spaces")
b=a.split(" ")
sum=0
for i in range(int(len_list)):
	sum+=int(b[i])

print(sum)