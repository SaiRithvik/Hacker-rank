string = input()

string2 = ''
for i in range(len(string)):

	if(string[i] == string[i].upper()):

		string2 += string[i].replace( string[i] , string[i].lower())
	
	else:

		string2 += string[i].replace(string[i] , string[i].upper())


print(string2)					

