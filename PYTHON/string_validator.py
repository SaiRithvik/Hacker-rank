s = input()

for i in range(len(s)):
	if(s[i].isalnum()):
		print(True)
		break
		
	else:
		if(i == len(s) - 1):

			print(False)
		continue


for i in range(len(s)):
	if(s[i].isalpha()):
		print(True)
		break
		
	else:
		if(i == len(s) - 1):

			print(False)
		continue

for i in range(len(s)):
	if(s[i].isdigit()):
		print(True)
		break
		
	else:
		if(i == len(s) - 1):

			print(False)
		continue

for i in range(len(s)):
	if(s[i].islower()):
		print(True)
		break
		
	else:
		if(i == len(s) - 1):

			print(False)
		continue

for i in range(len(s)):
	if(s[i].isupper()):
		print(True)
		break
		
	else:
		if(i == len(s) - 1):

			print(False)
		continue						



