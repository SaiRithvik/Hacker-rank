a = list((input()).split())

a.sort()

b = a.pop()


lowest_sum = 0
highest_sum = 0

for i in a:
    lowest_sum = lowest_sum + int(i)

a.append(b)

a.reverse()    

a.pop()

for j in a:
    highest_sum = highest_sum + int(j)


print(lowest_sum,end = ' ')
print(highest_sum)