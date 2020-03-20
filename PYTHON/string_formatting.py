def print_formatted(number):
    # your code goes here

    

    for j in range(1,n + 1):


        a = oct(j)

        b = a.split('o')

        octal = int(b[1])

        c = bin(j)

        d = c.split('b')

        binary = int(d[1])

        e = hex(j)

        f = e.split('x')

        hexadecimal = (f[1].upper())

    
        w = len(bin(n))


    #print(f'{j}{between}{octal}{between}{hexadecimal}{between}{binary}'.format(j,octal,hexadecimal,binary))
    
        print(f'{j}'.rjust(w-2,' '),end='')
        print(f'{octal}'.rjust(w-1,' '),end='')
        print(f'{hexadecimal}'.rjust(w-1,' '),end='')
        print(f'{binary}'.rjust(w-1,' '),end='\n')


if __name__ == '__main__':
	n = int(input())

	print_formatted(n)