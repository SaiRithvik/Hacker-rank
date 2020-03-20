#program to find runner-up score in list
a=[]

n = int(input())

if(n>=2 and n<=10):

	a = input()

	b = list(a.split(" "))

	winner_Score = int(b[0])

	for i in range(n):
	
		if(int(b[i])>winner_Score):
			winner_Score = int(b[i])

	count = 0

	for j in range(n):
		if(int(b[j]) == winner_Score):
			count = count + 1

	for k in range(count):

		b.remove(str(winner_Score))

	if(b == []):
		print(winner_Score)

	else:
		maximum = int(b[0])

		for m in range(len(b)):

			if(int(b[m])>maximum):

				maximum = int(b[m])
				
		print(maximum)		
			
