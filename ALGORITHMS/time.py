
q = input()


s = list(q.split(":"))

a = ''

if(s[2][2] =='P'):

	b = int(s[0])

	if(b != 12):
		b = b + 12  #hour

	s[0] = b

elif(s[2][2] == 'A'):
	
	b = int(s[0])

	if(b == 12):
		b = '0'

	s[0] = b	


a = q[2:8]

if(int(s[0]) > 9 ):

	a = str(s[0]) + a
else:
	a = '0' + str(s[0]) + a


print(a)


		

