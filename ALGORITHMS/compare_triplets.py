s1 = input()

lista = s1.split()

l1 = len(lista)

s2 = input()

listb = s2.split()

l2 = len(listb)

count_a = 0

count_b = 0

for i in range(l1):

    if(int(lista[i]) > int(listb[i])):

        count_a = count_a + 1

    elif(int(lista[i]) < int(listb[i])):

        count_b = count_b + 1

print(count_a,end=' ')
print(count_b)        






