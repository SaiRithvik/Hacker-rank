s , t = input().split()

a , b = input().split()

m , n = input().split()

s = int(s)
t = int(t)
a = int(a)
b = int(b)
m = int(m)
n = int(n)


d_apple = list(input().split())

d_orange = list(input().split())

count_apple = 0

count_orange = 0

for i in range(m):

	if((a+int(d_apple[i])) <= t and (a+int(d_apple[i])) >= s):

		count_apple = count_apple + 1

for i in range(n):

	if((b+int(d_orange[i])) <= t and (b+int(d_orange[i])) >= s):

		count_orange = count_orange + 1

print(count_apple)
print(count_orange)		


		