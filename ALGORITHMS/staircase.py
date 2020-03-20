
def space(k):
	for p in range(0 , k):
		
		
			print("", end=' ')
			
		

def staircase():
	n = int(input())

	for i in range(0 , n):
		space(n-i-1)
		print('#'*(i+1))
			
	
		

staircase()		

	
















