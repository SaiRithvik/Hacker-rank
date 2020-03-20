def count_substring(string, sub_string):

	l1 = len(string)
	l2 = len(sub_string)
	
	count = 0

	for i in range(l1):
		if(string[i:i+l2] == sub_string):
			count = count + 1

    
	return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)