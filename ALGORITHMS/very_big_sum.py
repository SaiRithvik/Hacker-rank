n = int(input())

arr = input()

sum = 0

list1 = arr.split(" ")

if(len(list1)>n):
	print("exceeded number of integers")
else:
	for i in range(len(list1)):
		sum += int(list1[i])

	print(int(sum))
	





