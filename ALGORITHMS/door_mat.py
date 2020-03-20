a= input()

n,m = a.split()




for i in range(int(n)):

	if(i < int(n)/2-1):

		print(('.|.'*(2*i+1)).center(int(m),'-'))

	elif(i == int(n)//2):

		print('WELCOME'.center(int(m),'-'))
		
	elif(i > int(n)/2):
		print(('.|.'*(2*(int(n)-i)-1)).center(int(m),'-'))		


